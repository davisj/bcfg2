"""This provides bcfg2 support for Solaris SYSV packages."""

import tempfile
from Bcfg2.Compat import any  # pylint: disable=W0622
import Bcfg2.Client.Tools
import Bcfg2.Client.XML
from Bcfg2.Compat import urlretrieve


# pylint: disable=C0103
noask = '''
mail=
instance=overwrite
partial=nocheck
runlevel=nocheck
idepend=nocheck
rdepend=nocheck
space=ask
setuid=nocheck
conflict=nocheck
action=nocheck
basedir=default
'''
# pylint: enable=C0103


class SYSV(Bcfg2.Client.Tools.PkgTool):
    """Solaris SYSV package support."""
    __execs__ = ["/usr/sbin/pkgadd", "/usr/bin/pkginfo"]
    __handles__ = [('Package', 'sysv')]
    __req__ = {'Package': ['name', 'version']}
    __ireq__ = {'Package': ['name', 'url', 'version']}
    name = 'SYSV'
    pkgtype = 'sysv'
    pkgtool = ("/usr/sbin/pkgadd %s -n -d %%s", (('%s %s', ['url', 'name'])))

    def __init__(self, logger, setup, config):
        Bcfg2.Client.Tools.PkgTool.__init__(self, logger, setup, config)
        # noaskfile needs to live beyond __init__ otherwise file is removed
        self.noaskfile = tempfile.NamedTemporaryFile()
        self.noaskname = self.noaskfile.name
        # for any pkg files downloaded
        self.tmpfiles = []
        try:
            self.noaskfile.write(noask)
            # flush admin file contents to disk
            self.noaskfile.flush()
            self.pkgtool = (self.pkgtool[0] % ("-a %s" % (self.noaskname)),
                            self.pkgtool[1])
        except:  # pylint: disable=W0702
            self.pkgtool = (self.pkgtool[0] % "", self.pkgtool[1])
        self.origpkgtool = self.pkgtool

    def pkgmogrify(self, packages):
        """ Take a list of pkg objects, check for a 'simplefile' attribute.
            If present, insert a _sysv_pkg_path attribute to the package and
            download the datastream format SYSV package to a temporary file.
        """
        for pkg in packages:
            if pkg.get('simplefile'):
                tmpfile = tempfile.NamedTemporaryFile()
                self.tmpfiles.append(tmpfile)
                self.logger.info("Downloading %s to %s" % (pkg.get('url'),
                                 tmpfile.name))
                urlretrieve(pkg.get('url'), tmpfile.name)
                pkg.set('_sysv_pkg_path', tmpfile.name)

    def _get_package_command(self, packages):
        """Override the default _get_package_command, replacing the attribute
           'url' if '_sysv_pkg_path' if necessary in the returned command
           string
        """
        if hasattr(self, 'origpkgtool'):
            if len(packages) == 1 and '_sysv_pkg_path' in packages[0].keys():
                self.pkgtool = (self.pkgtool[0], ('%s %s',
                                                  ['_sysv_pkg_path', 'name']))
            else:
                self.pkgtool = self.origpkgtool

        pkgcmd = super(SYSV, self)._get_package_command(packages)
        self.logger.debug("Calling install command: %s" % pkgcmd)
        return pkgcmd

    def Install(self, packages, states):
        self.pkgmogrify(packages)
        super(SYSV, self).Install(packages, states)

    def RefreshPackages(self):
        """Refresh memory hashes of packages."""
        self.installed = {}
        # Build list of packages
        lines = self.cmd.run("/usr/bin/pkginfo -x").stdout.splitlines()
        while lines:
            # Splitting on whitespace means that packages with spaces in
            # their version numbers don't work right.  Found this with
            # IBM TSM software with package versions like
            #           "Version 6 Release 1 Level 0.0"
            # Should probably be done with a regex but this works.
            version = lines.pop().split(') ')[1]
            pkg = lines.pop().split()[0]
            self.installed[pkg] = version

    def VerifyPackage(self, entry, modlist):
        """Verify Package status for entry."""
        desired_version = entry.get('version')
        if desired_version == 'any':
            desired_version = self.installed.get(entry.get('name'),
                                                 desired_version)

        if not self.cmd.run(["/usr/bin/pkginfo", "-q", "-v",
                             desired_version, entry.get('name')]):
            if entry.get('name') in self.installed:
                self.logger.debug("Package %s version incorrect: "
                                  "have %s want %s" %
                                  (entry.get('name'),
                                   self.installed[entry.get('name')],
                                   desired_version))
            else:
                self.logger.debug("Package %s not installed" %
                                  entry.get("name"))
        else:
            if self.setup['quick'] or \
               entry.attrib.get('verify', 'true') == 'false':
                return True
            rv = self.cmd.run("/usr/sbin/pkgchk -n %s" % entry.get('name'))
            if rv.success:
                return True
            else:
                output = [line for line in rv.stdout.splitlines()
                          if line[:5] == 'ERROR']
                if any(name for name in output
                       if name.split()[-1] not in modlist):
                    self.logger.debug("Package %s content verification failed"
                                      % entry.get('name'))
                else:
                    return True
        return False

    def Remove(self, packages):
        """Remove specified Sysv packages."""
        names = [pkg.get('name') for pkg in packages]
        self.logger.info("Removing packages: %s" % (names))
        self.cmd.run("/usr/sbin/pkgrm -a %s -n %s" %
                     (self.noaskname, names))
        self.RefreshPackages()
        self.extra = self.FindExtra()
