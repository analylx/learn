def m2u(mac_address)->'return the mac address with EUI64 format,64 bit':
    '''根据输入的mac地址，返回64位的EUI64格式的IPv6接口地址'''
    k = list(mac_address)
    k.insert(6,'fffe')
    eui64 = ''.join(k)
    # 这里还需要一步就是把次高位翻转，直接用二进制异或？
    return eui64

if __name__ == '__main__':
    print(m2u("00208f112233"))