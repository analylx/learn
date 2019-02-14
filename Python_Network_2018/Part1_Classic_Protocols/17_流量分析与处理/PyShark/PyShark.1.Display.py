#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# pyshark 特点分析
# 1.解码能力强,提供丰富的字段,远远强于Scapy
# 2.能够直接使用wireshark强大的display_filter
# 3.能够找到现象级数据包,例如重传 display_filter='tcp.analysis.retransmission'
# 3.能够使用wireshark的follow tcp stream的技术,找到特定tcp stream的数据包

# pyshark 问题
# 抓包在3.6环境出现问题
# 不能保存分析后的数据包到PCAP

import pyshark

#####################最原始操作,信息过量#####################
# cap = pyshark.FileCapture('dos.pcap')
#
# for pkt in cap:
#     print(pkt)
#     print(pkt.highest_layer)

#####################传一个函数,对pkt进行处理#####################
cap = pyshark.FileCapture('dos.pcap', keep_packets=False)  # 读取pcap文件,数据包被读取后,不在内存中保存!节约内存!


# 所有显示字段一览
# pkt
# ['__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_packet_string', 'captured_length', 'eth', 'frame_info', 'get_multiple_layers', 'get_raw_packet', 'highest_layer', 'http', 'interface_captured', 'ip', 'layers', 'length', 'number', 'pretty_print', 'show', 'sniff_time', 'sniff_timestamp', 'tcp', 'transport_layer']
# ip
# ['', 'DATA_LAYER', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_all_fields', '_field_prefix', '_get_all_field_lines', '_get_all_fields_with_alternates', '_get_field_or_layer_repr', '_get_field_repr', '_layer_name', '_sanitize_field_name', 'addr', 'checksum', 'checksum_status', 'dsfield', 'dsfield_dscp', 'dsfield_ecn', 'dst', 'dst_host', 'field_names', 'flags', 'flags_df', 'flags_mf', 'flags_rb', 'frag_offset', 'get', 'get_field', 'get_field_by_showname', 'get_field_value', 'hdr_len', 'host', 'id', 'layer_name', 'len', 'pretty_print', 'proto', 'raw_mode', 'src', 'src_host', 'ttl', 'version']
# tcp
# ['DATA_LAYER', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_all_fields', '_field_prefix', '_get_all_field_lines', '_get_all_fields_with_alternates', '_get_field_or_layer_repr', '_get_field_repr', '_layer_name', '_sanitize_field_name', 'ack', 'analysis', 'analysis_bytes_in_flight', 'analysis_initial_rtt', 'analysis_push_bytes_sent', 'checksum', 'checksum_status', 'dstport', 'field_names', 'flags', 'flags_ack', 'flags_cwr', 'flags_ecn', 'flags_fin', 'flags_ns', 'flags_push', 'flags_res', 'flags_reset', 'flags_str', 'flags_syn', 'flags_urg', 'get', 'get_field', 'get_field_by_showname', 'get_field_value', 'hdr_len', 'layer_name', 'len', 'nxtseq', 'payload', 'port', 'pretty_print', 'raw_mode', 'seq', 'srcport', 'stream', 'urgent_pointer', 'window_size', 'window_size_scalefactor', 'window_size_value']
# http
# ['', 'DATA_LAYER', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_all_fields', '_field_prefix', '_get_all_field_lines', '_get_all_fields_with_alternates', '_get_field_or_layer_repr', '_get_field_repr', '_layer_name', '_sanitize_field_name', '_ws_expert', '_ws_expert_group', '_ws_expert_message', '_ws_expert_severity', 'accept', 'accept_encoding', 'accept_language', 'chat', 'connection', 'cookie', 'cookie_pair', 'field_names', 'get', 'get_field', 'get_field_by_showname', 'get_field_value', 'host', 'layer_name', 'pretty_print', 'raw_mode', 'request', 'request_full_uri', 'request_line', 'request_method', 'request_number', 'request_uri', 'request_uri_path', 'request_uri_query', 'request_uri_query_parameter', 'request_version', 'user_agent']


def print_highest_layer(pkt):
    # 打印包中的特定字段
    print(pkt.highest_layer)
    print(pkt.ip.src_host)


# 把函数应用到数据包
cap.apply_on_packets(print_highest_layer)
