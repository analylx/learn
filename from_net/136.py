# -*- coding: utf-8 -*-
from typing import Dict
from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 第8章的网址
    url = 'http://www.136book.com/huaqiangu/ebxeew/'
    head: Dict[str, str] = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'}
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read()
    # 创建request对象,"html5lib" or 'lxml'
    soup = BeautifulSoup(html, "html5lib")

    # 找出div中的内容
    soup_text = soup.find('div', id='content')
    with open("136.txt", "w+") as fi:
        fi.write(soup_text.text)
