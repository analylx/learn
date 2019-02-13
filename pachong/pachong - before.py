#-*- coding: utf-8 -*-
"""
Created on 2016年8月11日
爬峨山一中贴吧啊
@author: pzy
"""

import requests
import re


class spider():
	def __init__(self):
		print('爬虫启动.......')

	def getSource(self, url):
		html = requests.get(url).text
		print("url转换成txt")
		return html

	def ChangePage(self, url, num_total):
		changePage = []
		for each_page in range(1, num_total + 1, 50):
			urlNow = re.sub('pn=(\d+)', 'pn=%s' % each_page, url, re.S)
			changePage.append(urlNow)
		return changePage

	def getmyideaInfo(self, source):
		li = re.findall('<li class=" j_thread_list clearfix"(.*?)</li>', source, re.S)
		return li

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

#要怎么样才能做到比较合适的单行注释或者行尾注释？
if __name__ == '__main__':
	classInfo = []
	"""url = 'http://tieba.baidu.com/f?kw=%E5%8F%8C%E6%B1%9F%E4%B8%AD%E5%AD%A6&ie=utf-8&pn=1'"""
	url = 'http://tieba.baidu.com/f?kw=amd'
	mySpider = spider()
	netPage = mySpider.ChangePage(url, 1000)
	for each in netPage:
		print('正在处理：' + each)
		html = mySpider.getSource(each)
		oppo = mySpider.getmyideaInfo(html)
		for i in oppo:
			info = mySpider.getinfo(i)
			classInfo.append(info)
		mySpider.saveinfo(classInfo)
