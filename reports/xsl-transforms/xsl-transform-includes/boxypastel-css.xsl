<?xml version="1.0"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:output method="html" indent="no"/>
<xsl:variable name="boxypastel-css">

<style type="text/css">
/* body */
body {
    background-color: #fff;
    color: #000;
    font: 12px 'Lucida Grande', Arial, Helvetica, sans-serif;
    margin-left:25px;
    margin-right:100px;
    }
/* links */
a:link {
    color: #00f;
    text-decoration: none;
    }
a:visited {
    color: #00a;
    text-decoration: none;
    }
a:hover {
    color: #00a;
    text-decoration: underline;
    }
a:active {
    color: #00a;
    text-decoration: underline;
    }
/* divs*/
div.bad {
    border: 1px solid #660000;
    background: #FF6A6A;
    margin: 10px 0;
    padding: 8px;
    text-align: left;
    margin-left:50px;
    margin-right:50px;
    }
div.modified {
    border: 1px solid #CC9900;
    background: #FFEC8B;
    margin: 10px 0;
    padding: 8px;
    text-align: left;
    margin-left:50px;
    margin-right:50px;
    }
div.clean {
    border: 1px solid #006600;
    background: #9AFF9A;
    margin: 10px 0;
    padding: 8px;
    text-align: left;
    margin-left:50px;
    margin-right:50px;
    }
div.extra {
    border: 1px solid #006600;
    background: #6699CC;
    margin: 10px 0;
    padding: 8px;
    text-align: left;
    margin-left:50px;
    margin-right:50px;
    }
div.warning {
    border: 1px solid #CC3300;
    background: #FF9933;
    margin: 10px 0;
    padding: 8px;
    text-align: left;
    margin-left:50px;
    margin-right:50px;
    }
div.all-warning {
    border: 1px solid #DD5544;
    background: #FFD9A2;
    margin: 10px 0;
    padding: 8px;
    text-align: left;
    margin-left:50px;
    margin-right:50px;
    }
div.down {
    border: 1px solid #999;
    background-color: #DDD;
    margin: 10px 0;
    padding: 8px;
    text-align: left;
    margin-left:50px;
    margin-right:50px;
    }
div.items	{
        display: none;
   }
div.nodebox {
    border: 1px solid #c7cfd5;
    background: #f1f5f9;
    margin: 20px 0;
    padding: 8px 8px 16px 8px;
    text-align: left;
    position:relative;
    }
div.header {
    background-color: #DDD;
    padding: 8px;
    text-indent:50px;
    position:relative;
    }
/*Divs For Statusbar*/
div.redbar {
    border: 0px solid #660000;
    background: #FF6666;
    margin: 0px;
    float: left;
    }
    
div.greenbar {
    border: 0px solid #006600;
    background: #66FF66;
    margin: 0px;
    float: left;
    }
div.statusborder {
    border: 1px solid #000000;
    background: #FF6666;
    margin: 0px;
    float: right;
    width: 100%;
    }
    /*invisitable*/
table.invisitable {
    width: 100%;
    border: 0px;
    cell-padding: 0px;
    padding: 0px;
    border-width: 0px;
    }
/*Spans*/
span.nodename {
    font-style: italic;
    }
span.nodelisttitle {
    font-size: 14px;
    }
span.mini-date {
    font-size: 10px;
    position: absolute;
    right: 65px;
    }

h2	{
    font-size: 16px;
    color: #000;
    }

ul.plain {
    list-style-type:none;
    text-align: left;
    }

.notebox {
    position: absolute;
    top: 0px;
    right: 0px;
    padding: 1px;
    text-indent:0px;
    border: 1px solid #FFF;
    background: #999;
    color: #FFF;
    }

.configbox {
    position: absolute;
    bottom: 0px;
    right: 0px;
    padding: 1px;
    text-indent:0px;
    border: 1px solid #999;
    background: #FFF;
    color: #999;
    }

p.indented{
    text-indent: 50px
    }

/* Sortable tables */
table.sortable a.sortheader {
    background-color:#dfd;
    font-weight: bold;
    text-decoration: none;
    display: block;

}  
table.sortable {
    padding: 2px 4px 2px 4px;
    border: 1px solid #000000;
    border-spacing: 0px
}
td.sortable{
    padding: 2px 8px 2px 8px;
}

th.sortable{
    background-color:#F3DD91;
    border: 1px solid #FFFFFF;
}
tr.tablelist {
    background-color:#EDF3FE;
}
tr.tablelist-alt{
    background-color:#FFFFFF;
}

</style>
</xsl:variable>
</xsl:stylesheet>

