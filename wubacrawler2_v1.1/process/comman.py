#-*- coding:utf-8 -*-

import re
import time
import requests

class PreProcessing(object):
    """
        基类 输入url获取html源码
             城市列表
    """

    def __init__(self):
        pass

    def get_html(self,url):

        times = 0
        wait_time = 60*8
        content = None

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0'}
        while times < 8:
            try:
                r = requests.get(url, timeout = 20, headers = headers)
                content = r.text
                return content
            except:
                times = times + 1
                time.sleep(wait_time)
        return content


    def get_city_name(self):

        url = "http://www.58.com/danbaobaoxiantouzi/changecity"
        r = requests.get(url)
        content = r.text

        #匹配onclick="co('cd')"
        city_name_list = re.findall(r"(?<=onclick\=\"co\(\').+?(?=\'\)\")", content)
        city_name_list = list(set(city_name_list))

        return city_name_list