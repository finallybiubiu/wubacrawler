# -*- coding:utf-8 -*-
"""
    获取浏览次数
"""
#http://jst1.58.com/counter?infoid=21860031008288
import requests
import time
import re

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

def get_html(url):
    """获取html源码"""
    times = 0
    wait_time = 30
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'Accept-Encoding': 'gzip, deflate'}

    while times < 5:
        try:
            r2 = requests.get(url, timeout = 20, headers = headers)
            return r2
        except:
            times = times + 1
            time.sleep(wait_time)

def get_view_counts(source_id):
    """获取浏览次数"""
    url = "http://jst1.58.com/counter?infoid=%s"%(source_id)
    r = get_html(url)
    content = r.content
    view_counts = re.findall(r'.*?total=([0-9]\d+)', content)
    view_counts = view_counts[0]
    return view_counts


def main():
    #把source_url首先存入文本文件中
    with open('', 'r') as f:
        for item in f:
            source_url = item.strip('\n')
            source_id = re.findall(r'.*?danbaobaoxiantouzi/([0-9]\d+)x.shtml', source_url)
            source_id = source_id[0]
            print "source_id",source_id
            view_counts = get_view_counts(source_id)

            info = WuBa.objects.using('saveinfo').filter(source_url = source_url)
            view_counts = int(view_counts)
            info[0].view_counts = view_counts
            #info[0].source_id = source_id
            info[0].save(using='saveinfo')


if __name__ == '__main__':
    main()

