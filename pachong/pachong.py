# -*- coding: utf-8 -*-
from typing import Dict, List, Any

import requests
import re


class spider():
    # 启动时打印提示信息，self参数是必须的，但无实际作用
    def __init__(self):
        print('爬虫启动.......')

    # 将url转换成txt的格式,返回text格式的html内容
    def getSource(self, url):
        html = requests.get(url).text
        print("url转换成txt")
        return html

    # 返回一个列表，
    def ChangePage(self, url, num_total):
        changePage = []
        for each_page in range(1, num_total + 1, 50):  # 使用+1来保证最后序列的最后一位的准确性
            # 首页地址	         http://tieba.baidu.com/f?kw=amd&ie=utf-8&pn=0
            # 原始的翻页url--http://tieba.baidu.com/f?kw=amd&ie=utf-8&pn=50
            # urlNow存储的是当前地址的
            urlNow = re.sub('pn=(\d+)', 'pn=%s' % each_page, url, re.S)
            changePage.append(urlNow)
        return changePage

    #
    def getmyideaInfo(self, source):
        li = re.findall('<li class=" j_thread_list clearfix"(.*?)</li>', source, re.S)
        return li

    # """findall()返回的是括号所匹配到的结果（如regex1），多个括号就会返回多个括号分别匹配到的结果，如果没有括号就返回就返回整条语句所匹配到的结果.只返回匹配的内容，不包括前后的描述条件"""
    # 参数re.S 它表示“.”（不包含外侧双引号，下同）的作用扩展到整个字符串，包括“\n”---正则表达式中，“.”的作用是匹配除“\n”以外的任何字符，也就是说，它是在一行中进行匹配。这里的“行”是以“\n”进行区分的。
    def getinfo(self, classinfo):
        info = {}
        info['最后回复时间'] = re.findall(
            '<span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">(.*?)</span>', classinfo, re.S)
        info['回复人数'] = re.findall('title="回复">(.*?)</span>', classinfo, re.S)
        info['主题'] = re.findall('target="_blank" class="j_th_tit ">(.*?)</a>', classinfo, re.S)
        info['主题作者'] = re.findall('title="主题作者:(.*?)"', classinfo, re.S)
        info['内容'] = re.findall('<div class="threadlist_abs threadlist_abs_onlyline ">(.*?)</div>', classinfo, re.S)
        info['最后回复人'] = re.findall(' <span class="tb_icon_author_rely j_replyer" title="最后回复人:(.*?)">', classinfo, re.S)
        return info

    def saveinfo(self, info):
        f = open('infoTieba.txt', 'a')
        for each in info:
            try:
                f.writelines('回复人数' + str(each['回复人数']) + '\n')
                f.writelines('主题' + str(each['主题']) + '/n')
                f.writelines('主题作者' + str(each['主题作者']) + '\n')
                f.writelines('内容' + str(each['内容']) + '\n')
                f.writelines('最后回复人' + str(each['最后回复人']) + '\n\n')
            except:
                pass
        f.close()


if __name__ == '__main__':  # 主程序的入口
    classInfo: List[Dict[str, List[Any]]] = []  # 一个列表用来存储什么的呢？每一个记录都是一篇帖子
    """url = 'http://tieba.baidu.com/f?kw=%E5%8F%8C%E6%B1%9F%E4%B8%AD%E5%AD%A6&ie=utf-8&pn=1'"""  # 这个是他原来的贴吧地址
    url = 'http://tieba.baidu.com/f?kw=amd&ie=utf-8&pn=0'  # 改成AMD吧的地址
    mySpider = spider()
    netPage = mySpider.ChangePage(url, 100)  # 每隔50页的图个url列表
    for each in netPage:
        print('正在处理：' + each)
        html = mySpider.getSource(each)  # 获取txt'格式的html页面内容
        oppo = mySpider.getmyideaInfo(html)  #
        for i in oppo:
            info = mySpider.getinfo(i)
            classInfo.append(info)
        mySpider.saveinfo(classInfo)
