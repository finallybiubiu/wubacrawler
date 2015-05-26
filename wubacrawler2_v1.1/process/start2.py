# -*- coding:utf-8


"""
    58_同城解析程序
"""

import threading
import os
import sys
import django
from os.path import dirname
reload(sys)
sys.path.append(dirname(dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "wubacrawler2.settings"
#django.setup()
from database.models import *
from process.parser_detail_html import *


def main(s,e):

    """
        解析code_0507数据库source_code表中的记录
        并把解析后的元素存入code_0507数据库中
    """

    business_info = {}
    business_detail_info = {}
    comp_info = {}
    list = SourceCode.objects.filter(flag=0)[s:e]
    print "ok"
    for i in range(len(list)):
        url_id = list[i].url_id
        content = list[i].source
        list[i].flag = 1
        list[i].save()

        business_info['url_id'] = url_id

        content = detail_html_slim(content)
        business_info = business_info_parser(content, business_info)
        business_detail_info = business_detail_info_parser(content, business_detail_info)
        comp_info = comp_info_parser(content, comp_info)

        info_save(business_info, business_detail_info, comp_info)


if __name__ == "__main__":
    step = 1000
    count = SourceCode.objects.filter(flag=0).count()
    print "Start!"
    print count
    pages = count / step + 2
    print pages
    for i in range(1, pages):
        s = i * step
        e = (i+1) * step
        main(s, e)
        print "结束%d"%i


# class WuBaParser(threading.Thread):
#     def __init__(self, startNum, endNum):
#         threading.Thread.__init__(self)
#         self.s = startNum
#         self.e = endNum
#     def run(self):
#         business_info = {}
#         business_detail_info = {}
#         comp_info = {}
#         lines = SourceCode.objects.filter(flag=0)[self.s:self.e]
#
#         for line in lines.iterator():
#
#             url_id = line.url_id
#             content = line.source
#             line.flag = 1
#             line.save()
#             print url_id
#
#             business_info['url_id'] = url_id
#
#             content = detail_html_slim(content)
#             business_info = business_info_parser(content, business_info)
#             business_detail_info = business_detail_info_parser(content, business_detail_info)
#             comp_info = comp_info_parser(content, comp_info)
#
#             info_save(business_info, business_detail_info, comp_info)
#
# if __name__ == "__main__":
#     count = SourceCode.objects.filter(flag=0).count()
#     print "Start!"
#     print count
#
#     p1 = WuBaParser(0,1000)
#     p1.start()
