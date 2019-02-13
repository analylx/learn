import paramiko,time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("172.96.226.27",29316, "root", "Tqwbg3XP8j7G")

#stdin, stdout, stderr = ssh.exec_command("cd /;pwd")
#records1 = stdout.readlines()
#print records1

#stdin, stdout, stderr = ssh.exec_command("lsh;configure;run show bfd session")
chan = ssh.invoke_shell()

chan.send('pwd\n')
#chan.send('run show bfd session\n')
time.sleep(3)
records = chan.recv(5000)
#records = stdout.readlines()
#print ("records is " + str(records))

ssh.close()
#stdin, stdout, stderr = ssh.exec_command("ls")

f = open('records3.txt', 'a+')
f.write(str(records))
#python2 is fine with f.write(each). But for python3 it write all the numbers.
f.close()