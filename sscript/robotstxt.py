"""testing for robots.txt"""
import requests


def run(url):
    robots_url = '%s://%s/robots.txt' % (url.scheme, url.netloc)
    result = requests.get(robots_url)

    return '%s\n%s' % (result.status_code, result.content)
