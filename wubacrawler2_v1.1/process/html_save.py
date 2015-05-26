# -*- coding:utf-8 -*-

"""
    处理详细页
"""

import copy
from process.list_page import *
from comman import PreProcessing

import hashlib
import os
import sys
import django
from os.path import dirname
reload(sys)
sys.path.append(dirname(dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "wubacrawler2.settings"
#django.setup()
from database.models import *


class FetchDetailHtml(PreProcessing):

    """
        解析html源码
    """

    def __init__(self, r, url_set):
        PreProcessing.__init__(self)
        self.r = r
        self.url_set = url_set
        self.wait_time = 1
        self.flag = True

    def get_detail_url(self):
        if self.r.scard(self.url_set)!= 0:
            url = self.r.spop(self.url_set)
            if url is not None:
                url = url + '.shtml'
                return url
        else:
            time.sleep(self.wait_time)
            url = self.r.spop(self.url_set)
            if url is not None:
                url = url + '.shtml'
                return url


    def detail_html_parser(self):

        source_detail_info = {}
        source_code_info = {}

        detail_url = self.get_detail_url()
        content = self.get_html(detail_url)
        source_detail_info['url'] = detail_url
        #print detail_url

        m = hashlib.md5()
        m.update(detail_url)
        url_md5 = m.hexdigest()
        source_detail_info['url_md5'] = url_md5
        source_code_info['source'] = content


        source_detail_save(source_detail_info)

        source_code_save(source_code_info, source_detail_info)

    def parser_to_save(self):
        while self.flag:
            self.detail_html_parser()
            time.sleep(2)
            self.stop()

    def stop(self):
        if self.r.scard(self.url_set) == 0:
            self.flag = False
            print "end"
        else:
            self.flag = True


