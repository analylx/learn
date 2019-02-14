#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""@doc!
通过命令行升级NPTI设备。
输入参数：
1.ne_type 设备类型(1800/1200i/1050i/1300)
2.ne_version 目标版本(可自动去版本文件夹取最新版本)
3.ne_ip_address 网元地址

特性：
1.传完版本后自动sync，并确认提示符
2.判断当前MCP的主用半区(通过startup文件)，只传主用半区
3.从arp获取的值中判断需要登陆的备卡
4.重启之前保存当前配置到sdboot
5.使用show  version确认版本信息可读取并是在主用半区
6.通过run show sytem status确认系统正常启动后，加载保存的配置。后续如果不请空的话，可以判断是否被清空再执行。
7.检查网元HA的情况，下载并升级相应的版本（1+1或者2+0）.备卡不在位时，超时重试
8.自动根据版本判断登陆的用户名和行为

查询BFD状态和LSP ping结果
"""
import os
import re

#需要全局使用的变量，尽量赋给初始值
startup_field = "up"#启动半区，up/donw,默认是up
ne_type = "1800"
ne_version =""#需要升级的版本
ne_ip_address = ""#200.200.180.58
standby_mcp_ip = ""#169.254.1.3

def sync_and_wait():
    pass

def check_startup_file():
    pass
    
def get_version():
    pass

def download_to_ne():
    pass

def check_standby_mcp():
    return standby_mcp_ip
