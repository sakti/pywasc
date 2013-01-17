"""testing for robots.txt"""
import time


def run(*args, **kwargs):
    result = str(args)
    time.sleep(3)
    result += str(kwargs)
    return result
