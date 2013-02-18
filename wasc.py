#!/usr/bin/env python
import os
import sys
import argparse
import time
import cgi
from urlparse import urlparse
from datetime import datetime


__VERSION__ = "0.1"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_DIR = os.path.join(ROOT_DIR, 'sscript')

parser = argparse.ArgumentParser(
            prog="pywasc",
            description="Web Application Security Scanner"
         )
parser.add_argument("-u", "--url",
            action="store",
            help="target url",
            required=True)
parser.add_argument("-o", "--output",
            action="store",
            help="output report (html)",
            default="report.html")
parser.add_argument("-v", "--version",
            action="version",
            version=__VERSION__)


def get_list_script():
    "search module in ``script`` directory"
    list_script = []
    for item in os.listdir(SCRIPT_DIR):
        path = os.path.join(SCRIPT_DIR, item)
        if (item.endswith(".py") and
            item != '__init__.py' and
            os.path.isfile(path)):
            item = item[:-3]
            tmpmodule = __import__('sscript.%s' % item)
            tmpmodule = getattr(tmpmodule, item)
            try:
                getattr(tmpmodule, 'run')
                getattr(tmpmodule, '__id__')
                getattr(tmpmodule, '__desc__')
                list_script.append(tmpmodule)
            except:
                continue
    # ordering based on script id
    list_script.sort(key=lambda x: x.__id__)
    return list_script


if __name__ == "__main__":
    args = parser.parse_args()
    url = urlparse(args.url)

    if url.scheme not in ["http", "https"]:
        print "supported protocols are http and https"
        sys.exit(2)

    report_file = open(args.output, 'w')
    report_file.write("""
    <html><head><title>pyWasc Report</title></head>
    <style>
        body{
            font-size:14px;
            line-height:20px;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        pre {
            padding: 0 3px 2px;
            font-family: Monaco, Menlo, Consolas, "Courier New", monospace;
            font-size:12px;
            color: #333;
            border-radius:3px;
            white-space: pre;
            white-space: pre-wrap;
            }
    </style>
    <body>
    <h1>pyWasc Report on %s</h1>
    """ % args.url)

    scripts = get_list_script()

    start_time = time.time()

    for script in scripts:
        script_name = script.__name__.split('.')[1]
        print "Execute scan script %s" % script_name
        report_file.write('<hr>')
        report_file.write("<h3>Execute scan script %s</h3>" % script_name)
        report_file.write("<p>%s</p>" % script.__desc__)
        start_script = datetime.now()
        result = script.run(url)
        end_script = datetime.now()
        result = cgi.escape(result)
        report_file.write('<pre>%s</pre>' % result)
        report_file.write('<p>%s - %s</p>' % (start_script, end_script))
        report_file.write('<p>Duration: %s</p>' % (end_script - start_script))

    end_time = time.time()

    print "Duration: %s" % (end_time - start_time)

    report_file.write("<hr>")
    report_file.write("Total Duration: %s" % (end_time - start_time))
    report_file.write("</body></html>")

    report_file.close()
