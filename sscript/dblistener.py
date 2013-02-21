"""Look for well-known database open port on target host"""
from sh import nmap


__id__ = 5
__author__ = 'Sakti Dwi Cahyono'


ports = {
    1433: 'MSSQL server',
    1434: 'MSSQL monitor',
    1521: 'Oracle listener',
    1526: 'Oracle listener alternative',
    2424: 'OrientDB listener binary',
    2480: 'OrientDB lintener http',
    2483: 'Oracle lintener(future)',
    2484: 'Oracle lintener(future) ssl',
    2638: 'Sybase db listener',
    3306: 'MySQL',
    5432: 'PostgreSQL',
    5984: 'CouchDB',
    6262: 'Sybase Advantage Db Server',
    12010: 'ElevateDB',
    27017: 'MongoDB'
}


def run(url):
    result = ''
    for port in ports:
        result += '%s' % ports[port]
        result += nmap(url.hostname, p=port).stdout
        result += '\n'

    return '%s' % result
