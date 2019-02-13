#!/usr/bin/env python
# encoding: utf-8
 
# 把str编码由ascii改为utf8（或gb18030）
import sys
reload(sys)
sys.setdefaultencoding('utf8')
 
import time
import re
import requests
from bs4 import BeautifulSoup
 
file_name = 'book_list.txt'
file_content = '' # 最终要写到文件里的内容
file_content += '生成时间：' + time.asctime()
 
def book_spider(book_tag):
    global file_content
 
    url = "http://book.douban.com/tag/%s?type=S" % book_tag
    source_code = requests.get(url)
    # just get the code, no headers or anything
    plain_text = source_code.text
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text)
    '''print('\n')
    print('--' * 30)
    print('--' * 30)
    print("\t"*4+book_tag+" :")
    print('--' * 30)
    print('--' * 30)
    print('\n')'''
    title_divide = '\n' + '--' * 30 + '\n' + '--' * 30 + '\n'
    file_content += title_divide + '\t' * 4 + \
            book_tag + '：' + title_divide
    count = 1
    for book_info in soup.findAll('div', {'class': 'info'}):
        title = book_info.findAll('a', {
            'onclick': re.compile(r"\"moreurl(.+)")})[0].get('title')
 
        pub = book_info.findAll('div', {'class':'pub'})[0].string.strip()
        rating = book_info.findAll('span', {
            'class':'rating_nums'})[0].string.strip()
        people_num = book_info.findAll('span', {
            'class':'pl'})[0].string.strip()
        file_content += "*%d\t《%s》\t评分：%s%s\n\t%s\n\n" % (
                count, title, rating, people_num, pub)
        count += 1
 
 
# 此函数并未使用。若需要抓取书籍详情页面的信息，
# 可在以下代码的基础上进一步完善。
def get_single_book_data(book_url):
    source_code = requests.get(book_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
#    for rating in soup.findAll('strong', {'class':'ll rating_num '}):
#        print("评分：" + rating.string.strip())
    for rating in soup.findAll('p', {'class':'rating_self clearfix'}):
        print rating.strong.string
    '''for book_info in soup.findAll('div', {'id':'info'}):
        if book_info != None:
            info = book_info.string
            print("详情：" + info)'''
 
def do_spider(book_lists):
    for book_tag in book_lists:
        book_spider(book_tag)
 
book_lists = ['心理学','人物传记','中国历史','旅行','生活','科普']
do_spider(book_lists)
 
# 将最终结果写入文件
f = open(file_name, 'w')
f.write(file_content)
f.close()
#get_single_book_data('http://book.douban.com/subject/4242172/')