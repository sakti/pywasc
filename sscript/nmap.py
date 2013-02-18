"""testing for robots.txt"""
from sh import nmap


__id__ = 2
__author__ = 'Sakti Dwi Cahyono'
__desc__ = 'Look for open port on target host'


def run(url):
    result = nmap(url.netloc)

    return '%s' % result.stdout
