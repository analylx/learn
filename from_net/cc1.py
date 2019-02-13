#! /usr/bin/env python 
# -*- coding: UTF-8 -*- 

import paramiko,os,re,time

class RCPD_Exception(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return self.value

class CFGD_Exception(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return self.value 

#check进程的函数，进程stuck会报异常，每ss(s>2)秒check一次
def check(hostname,ss):
    hostname=hostname
    port = 26831
    username = 'root'
    password = 'ZrTaYjkAamiS'
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname,port,username,password)
    ssh = s.invoke_shell()
    ss-=2
    while(1):
        time.sleep(ss)
        ssh=s.invoke_shell()
        ssh.send('ps -ef\n')
        time.sleep(2)
        x = ssh.recv(10000)
        pattern1=re.compile(r'(./usr/sbin/sshd|\[crond\])')
        crond=re.findall(pattern1,x)
        print ('crond state: ',crond,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        pattern2=re.compile(r'(./usr/libexec/postfix/master|\[cfgd\])')
        cfgd=re.findall(pattern2,x)
        print ('cfgd state: ',cfgd,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        print crond[0]
        if not crond[0]==' /usr/sbin/sshd':
            try:
                raise RCPD_Exception('RCPD stuck')
            except RCPD_Exception,e:
                print e

        if not cfgd[0]==' /usr/libexec/postfix/master':
            try:
                raise CFGD_Exception('CFGD stuck')
            except CFGD_Exception,e:
                print e


if __name__=='__main__': 
    ss=int(raw_input('Please put into the interval checktime(larger than 2s)/s:'))
    check('93.179.102.65',ss)