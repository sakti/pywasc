"""Look for open port on target host"""
from sh import nmap


__id__ = 1
__author__ = 'Sakti Dwi Cahyono'


def run(url):
    result = nmap(url.hostname)

    return '%s' % result.stdout
