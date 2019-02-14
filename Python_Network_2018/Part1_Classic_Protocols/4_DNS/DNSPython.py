#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import dns.resolver


def dnspython(domain, Type="A"):
    result = dns.resolver.query(domain, Type)
    return_result = []
    if Type == "A" or Type == "AAAA":
        for i in result.response.answer:
            for j in i.items:
                return_result.append(j.address)
    elif Type == "CNAME" or Type == "NS":
        for i in result.response.answer:
            for j in i.items:
                return_result.append(j.to_text())
    elif Type == 'MX':
        for i in result:
            return_result.append({'MX preference':i.preference, 'mail exchanger':i.exchange.to_text()})
    return return_result


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    print(dnspython("cisco.com", Type="A"))
    print(dnspython("cisco.com", Type="AAAA"))
    print(dnspython("www.cisco.com", Type="CNAME"))
    print(dnspython("cisco.com", Type="NS"))
    print(dnspython("cisco.com", Type="MX"))
