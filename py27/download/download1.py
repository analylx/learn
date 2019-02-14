#-*- coding: utf-8 -*-

import requests
import time

file1=open('address.txt')

for addr in file1.readlines():
    print addr
    try:
        r = requests.get(addr.strip(),stream=True,timeout=30) # create HTTP response object
        local_name = addr.split('/')[-1]
        
        with open(local_name.strip(),'wb+') as f:
            #用这种方式打开文件不需要显式地关闭文件么？
            f.write(r.content)
        print "%s is download." %local_name.strip()
        #time.sleep(5)
    except Exception,e:
        print 'Cannot download%s '%addr

file1.close()