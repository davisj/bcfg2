"""Base modules definition."""

from Bcfg2.Compat import walk_packages
__all__ = [m[1] for m in walk_packages(path=__path__)]
