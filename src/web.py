# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# @File    :   web.py
# @Time    :   2023/03/06 12:34:48
# @Author  :   TKkk 
# @Email   :   tkk.ioser@gmail.com

import os, json
import requests

def get(url):
    data = requests.get(url).text
    return json.loads(data)

def post(url, data):
    data = requests.post(url, data)
    return data

def main():
    None

if __name__ == "__main__":
    main()