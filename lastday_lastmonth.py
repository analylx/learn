from datetime import datetime
from datetime import timedelta
import calendar
import logging
import os.path
import time
logging.basicConfig(level=10,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.debug("默认只显示到warning")


def getLastDayOfLastMonth():
    d = datetime.now()+timedelta(weeks=300)#往后多少时间，默认是天
    logging.info("the value of d: %s",d)
    #c = calendar.Calendar()

    year = d.year
    month = d.month
    logging.info("the value of month: %s",month)
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1
    days = calendar.monthrange(year, month)[1]
    logging.info("the value of days: %s",days)
    logging.info("the value of datetime(year, month, 1): %s",datetime(year, month, 1))
    logging.info("the value of timedelta(1): %s",timedelta(days))   
    return (datetime(year, month, 1)+timedelta(days=(days-1))).strftime('%Y-%m-%d %X')


if __name__ == "__main__":
    logging.error("oooop error")
    print(getLastDayOfLastMonth())
    #以下步骤是将日志写入到文件
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级开关
    # 第二步，创建一个handler，用于写入日志文件
    logging.info("the value of time is : %s",time.time())
    logging.info("the value of time.localtime(time.time()) is : %s",time.localtime(time.time()))
    datetime_now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    logging.info("the value of datetime_now is : %s",datetime_now)
    log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    log_name = log_path + datetime_now + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)
    # 日志
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')
