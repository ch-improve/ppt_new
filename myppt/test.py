import json
import os
import sys

import requests


def test():
    body = {'id': '2', 'path': '/home/ppt_jpg/ppt_new/myppt/static/ppt'+'20191009-1.pptx'}
    res = requests.post('127.0.0.1:9876/index/', json.dumps(body)).content.decode()
    print(res)


def test2():
    res = requests.get('127.0.0.1:9876/index/?id=2').content.decode()
    print(res)


if __name__ == '__main__':
    s = sys.argv[1]
    if s == 'post':
        test()
    elif s == 'get':
        test2()
