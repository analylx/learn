# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 目录页
    url = 'http://www.136book.com/huaqiangu/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers = head)
    response = request.urlopen(req)
    html = response.read()
    # 解析目录页
    soup = BeautifulSoup(html, 'lxml')
    # find_next找到第二个<div>
    soup_texts = soup.find('div', id = 'book_detail', class_= 'box1').find_next('div')
    # 遍历ol的子节点，打印出章节标题和对应的链接地址
    fi = open("chapter_list.txt",'w+')
    for link in soup_texts.ol.children:
        if link != '\n':
            cont = str(link.text) + ':  '+ link.a.get('href')+"\n"
            #print(cont)
            fi.writelines(cont)
    fi.close()