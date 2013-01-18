"""testing for robots.txt"""
from sh import nmap


def run(url):
    result = nmap(url.netloc)

    return '%s' % result.stdout
