import time
from poplib import POP3_SSL
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# from csv import excel
# from symbol import except_clause

popServerAddress = 'pop.126.com'
emailAddress = input('Please input mail  address:')
pwd = input('Please input the password')
# 连接服务器，如果3秒连不上就退出
server = POP3_SSL(popServerAddress, timeout=3)
server.set_debuglevel(1)
# 模拟登陆
server.user(emailAddress)
server.pass_(pwd)
# 获取最新2000封邮件的编号，mails的格式为['mesg_num octets',...]
_, mails, _ = server.list()
# 由于我的邮件很少，所以把总数改成200
mailNums = list(map(lambda item: int(item.split()[0]), reversed(mails)))[:200]
# 用来存储邮件日期的文件
fp = open('date.txt', 'w')
# 遍历所有的文件
for num in mailNums:
    try:
        # lines是一个字符串列表，存放了该邮件的所有行
        _, lines, _ = server.retr(num)
    except:
        # 跳过失败的个别邮件
        continue
    for line in lines:
        line = line.strip()
        if line.startswith(b'Date:'):
            receiveTime = line.decode()[5:]
            break
    else:
        continue
    # 适当修订不合适的日期格式
    dt = receiveTime[:30].split()
    if len(dt) < 5:
        continue
    if len(dt[3]) == 2:
        dt[3] = '20' + dt[3]
    receiveTime = ''.join(dt)
    try:
        # receiveTime = time.strptime(receiveTime[0:receiveTime.rindex(':')+3].strip(), '%a, %d %b %Y %H:%M:%S')
        # 遇到的问题是格式的对应需要看实际运行的输出和预期值之间的严格差异.ValueError: time data 'Fri,1Jun201817:46:20' does not match format '%a,%b%d%Y%H:%M:%S'
        receiveTime = time.strptime(receiveTime[0:receiveTime.rindex(':') + 3].strip(), '%a,%d%b%Y%H:%M:%S')
    except:
        # receiveTime = time.strptime(receiveTime[0:receiveTime.rindex(':')+3].strip(), '%d %b %Y %H:%M:%S')
        receiveTime = time.strptime(receiveTime[0:receiveTime.rindex(':') + 3].strip(), '%d%b%Y%H:%M:%S')

    receiveTime = time.strftime('%Y:%m:%d %H:%M:%S', receiveTime)
    # 只关心年份和月份
    ymd = receiveTime[:7]
    print(ymd)
    fp.write(ymd + '\n')
fp.close()
server.quit()

# 读取获取的时间数据
with open('date.txt') as fp:
    dateFrequency = fp.read().split()
# 绘制折线图
df = pd.DataFrame({'年月': dateFrequency, '数量': [1] * len(dateFrequency)})
df = df.groupby('年月', as_index=False).sum()
df.plot(x='年月', kind='bar')
font = FontProperties(fname="C:\Windows\Fonts\simsunb.ttf")
plt.legend(prop=font)
plt.show()
