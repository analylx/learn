import subprocess
import uuid
import logging
logging.basicConfig(
    level=14,
    format=
    '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def get_mac_info():
    mac_info = subprocess.check_output('GETMAC /v /FO list',
                                       stderr=subprocess.STDOUT)
    logging.debug("mac_info is: %s", mac_info)#这里的%s不能去掉，否则会报参数过多的错误
    print('Your MAC address:', mac_info)


if __name__ == "__main__":
    get_mac_address()
    get_mac_info()