#-*- coding: utf-8 -*-

import paramiko,time

Host = "200.200.180.58"
Port = 22
user = "admin"
password = "admin1"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(Host, Port, user, password)

stdin, stdout, stderr = ssh.exec_command("show bfd session terse")
#Time = str(ssh.exec_command("date"))
#print(Time)
records = stdout.readlines()
#print records
# the result:   ['/home/fs\n']

stdin, stdout, stderr = ssh.exec_command("ls")
#print records
with open("ifconfig.txt", 'a') as f:
    for each in records:
        try:
            f.write(str(each)+ '\n')
        except:
            pass
