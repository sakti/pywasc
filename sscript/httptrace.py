"""Check if http trace enabled in web server"""
import requests


__id__ = 3
__author__ = 'Sakti Dwi Cahyono'


def run(url):
    root_url = '%s://%s' % (url.scheme, url.netloc)
    result = requests.request('trace',
            root_url, cookies={'msg': 'Echoed back'})

    return '%s\n%s' % (result.status_code, result.content)
