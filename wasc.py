#!/usr/bin/env python
import os
import sys
import argparse
import time
from urlparse import urlparse


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
    list_script = {}
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
                list_script[item] = tmpmodule
            except:
                continue
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
    <body>
    <h1>pyWasc Report on %s</h1>
    """ % args.url)

    scripts = get_list_script()

    start_time = time.time()
    for script in scripts:
        print "Execute scan script %s" % script
        report_file.write("<h3>Execute scan script %s</h3>" % script)
        result = scripts[script].run(url)
        report_file.write('<pre>%s</pre>' % result)
    end_time = time.time()
    print "Duration: %s" % (end_time - start_time)
    report_file.write("Duration: %s" % (end_time - start_time))
    report_file.write("</body></html>")

    report_file.close()
