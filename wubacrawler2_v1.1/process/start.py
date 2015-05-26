# -*- coding:utf-8 -*-

"""
    start.py获取详细页html源码的程序
    存放在数据库code_0507里面

    start2.py对详细页html源码解析
    存放在数据库code_0507里面

    功能:先爬取……后解析……
"""

import redis
import time
from process.html_save import FetchDetailHtml
from process.list_page import SummaryFetchParse

def main():
    """
        爬取详细页源码 存入code_0507数据库中
    """

    r = redis.Redis(host = 'localhost', port = 6379, db = 1)
    r.flushdb()
    url_set = set()


    #河南省 + 新疆省
    #湖北省 + 湖南省 + 黑龙江省 + 吉林省 +广东省
    #四川省 + 云南省 + 贵州省 + 陕西省

    #城市简称列表
    city_name_list = ['bt','chifeng','erds','hu','sjz','xj','changji','bygl','yili','aks',
                      'ks','hami','klmy','betl','tlf','ht',
                      'shz','kzls','ale','wjq','tmsk',
                      'ganzhou','nc','liuzhou','qinzhou','haikou',
                      'zz','luoyang','xx',]

    #城市简称字典
    city_dict = {'bt':24,'chifeng':32,'erds':13,'hu':48,'sjz':70,'xj':70,'changji':6,'bygl':7,'yili':5,'aks':6,
                 'ks':4,'hami':4,'klmy':4,'betl':4,'tlf':4,'ht':4,
                 'shz':6,'kzls':3,'ale':3,'wjq':3,'tmsk':3,
                 'ganzhou':31,'nc':70,'liuzhou':46,'qinzhou':5,'haikou':23,
                 'zz':70,'luoyang':28,'xx':12,}

    while len(city_name_list) > 0:
        city_name = city_name_list.pop()
        print "======城市%s爬取开始======"%(city_name)
        page_nums = city_dict.get(city_name)
        page_num_start = 1
        page_num_end = 2

        while page_num_start <= page_nums:

            p1 = SummaryFetchParse(r, url_set, page_num_start, page_num_end)
            p1.get_city_list(city_name)

            p2 = FetchDetailHtml(r, url_set)
            p2.parser_to_save()


            print "*********本次爬取结束***********"
            time.sleep(60*1)
            page_num_start = page_num_end + 1
            page_num_end = page_num_end + 2

        print "=====城市%s爬取结束====="%(city_name)


if __name__ == "__main__":
    main()


