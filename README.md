pywasc
======

python web application security scanner



Requirements
------------

- requests
- sh


Usage
-----

    usage: wasc [-h] -u URL [-o OUTPUT] [-v]

    Web Application Security Scanner

    optional arguments:
      -h, --help            show this help message and exit
      -u URL, --url URL     target url
      -o OUTPUT, --output OUTPUT
                            output report (html)
      -v, --version         show program's version number and exit

Example: 

    $python wasc.py -u http://localhost -o report_localhost.html


Documentation
-------------

[Read the docs](https://pywasc.readthedocs.org/en/latest/)
