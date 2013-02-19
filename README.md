pywasc
======

Web application security scanner.



Requirements
------------

Python modules:

- requests
- sh


Usage
-----

    usage: wasc.py [-h] [-s SSCRIPT] -u URL [-o OUTPUT] [-v]

    Web Application Security Scanner

    optional arguments:
      -h, --help            show this help message and exit
      -s SSCRIPT, --sscript SSCRIPT
                            run specific scan script
      -u URL, --url URL     target url
      -o OUTPUT, --output OUTPUT
                            output report (html)
      -v, --version         show program's version number and exit

Example: 

    $python wasc.py -u http://localhost -o report_localhost.html

run specific sscript

    $./wasc.py -s sscript/httptrace.py -u http://localhost -o http_trace_local.html


Documentation
-------------

[Read the docs](https://pywasc.readthedocs.org/en/latest/)
