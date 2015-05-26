# -*- coding:utf-8 -*-
"""
    58同城汇总程序
    表模型为:WuBa
"""

import uuid
import os
import sys
import django
import threading
from os.path import dirname
reload(sys)
sys.path.append(dirname(dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "wubacrawler2.settings"
#django.setup()
from database.models import *


import hashlib
def md5(content):
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()

class WuBaFinal(threading.Thread):
    def __init__(self, startNum, endNum):
        threading.Thread.__init__(self)
        self.s = startNum
        self.e = endNum

    def run(self):

        info = {}
        info_list = BusinessInfo.objects.using('default').filter(flag=0)[self.s:self.e]

        for item in info_list:
            info = {'id':str(uuid.uuid4()),
                    'comp_name':item.comp_name.comp_name,
                    'reg_time':item.comp_name.reg_time,
                    'reg_address':item.comp_name.reg_address,
                    'comp_url':item.comp_name.comp_url,
                    'shop_url':item.comp_name.shop_url,
                    'source_url':item.url.url,
                    'source_url_mapping':md5(item.url.url.encode('utf-8')),
                    'business_name':item.business_name,
                    'business_released_date':item.business_released_date,
                    'link_people':item.link_people,
                    'telephone':item.telephone,
                    'father_type':item.father_type,
                    'reservation_counts':item.reservation_counts,
                    'view_counts':item.view_counts,
                    'child_type':item.child_type,
                    'business_detail_id':item.business_detail.id,
                    'comp_name_id':item.comp_name.id,
                    'url_id':item.url.id}
            #print info
            item.flag =1
            item.save(using='default')
            wuba_info_save(info)



def main():

    #58同城汇总程序：

    count = BusinessInfo.objects.using('default').filter(flag=0).count()
    print "Start!"
    print count
    p1 = WuBaFinal(0,10000)
    p1.start()
    p2 = WuBaFinal(10000,30000)
    p2.start()
    p3 = WuBaFinal(30000,60000)
    p3.start()
    p4 = WuBaFinal(60000,95575)
    p4.start()



if __name__ == '__main__':
    main()
