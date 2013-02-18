"""testing for robots.txt"""
import requests


__id__ = 2
__author__ = 'Sakti Dwi Cahyono'
__desc__ = 'Check if robots.txt contain secret data'


def run(url):
    robots_url = '%s://%s/robots.txt' % (url.scheme, url.netloc)
    result = requests.get(robots_url)

    return '%s\n%s' % (result.status_code, result.content)
