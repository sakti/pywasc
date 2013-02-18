"""Check http only flag in cookie"""
import requests


__id__ = 4
__author__ = 'Sakti Dwi Cahyono'


def run(url):
    result = requests.get(url.geturl())
    result_txt = 'cookies: \n========\n'

    for cookie in iter(result.cookies):
        result_txt += "%s: %s, domain=%s, secure=%s, HttpOnly=%s\n" % (
            cookie.name,
            cookie.value,
            cookie.domain,
            cookie.secure,
            'OK' if cookie.has_nonstandard_attr('HttpOnly') else 'NOT set')

    return result_txt
