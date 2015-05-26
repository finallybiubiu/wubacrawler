#-*- coding:utf-8 -*-

"""
    处理摘要页
"""

from process.comman import *


class SummaryFetchParse(PreProcessing):
    """摘要页爬虫解析 传入城市简称"""
    def __init__(self, r, url_set, page_num_start, page_num_end):
        PreProcessing.__init__(self)
        self.page_num = page_num_start
        self.page_num_end = page_num_end
        self.wait_time = 5
        self.r = r
        self.url_set = url_set
        self.flag = True

    def summary_html_parser(self, content, url_set):

        url_list = re.findall(r"(?<=a\shref=\')(.+?)\.shtml", content)

        for url in url_list:
            if len(url)>0:
                self.r.sadd(url_set,url)
        return len(url_list)

    def get_city_list(self, city_name):

        url = 'http://%s.58.com/danbaobaoxiantouzi/pn%d'%(city_name, self.page_num)
        content = self.get_html(url)
        lens = self.summary_html_parser(content,self.url_set)
        print "list len is", lens

        while self.page_num < self.page_num_end:

            self.page_num = self.page_num + 1

            print "page is", self.page_num
            url = 'http://%s.58.com/danbaobaoxiantouzi/pn%s'%(city_name, self.page_num)
            content = self.get_html(url)
            lens = self.summary_html_parser(content, self.url_set)
            time.sleep(self.wait_time)
            print "list len is", lens
        print "*****Detail-Finish******"
























