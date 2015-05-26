# -*- coding:utf-8 -*-

import re
import time
import datetime
import redis
import requests
import uuid
from process.list_page import *
from comman import PreProcessing

import hashlib
import os
import sys
import django
from os.path import dirname
reload(sys)
sys.path.append(dirname(dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "wu_ba_crawler.settings"
#django.setup()

from database.models import *

def detail_html_slim(content):
    """
     对html源码瘦身
    """
    content = re.sub(r"\n|\t|\r", " ", content)
    content = re.sub(r"<br.*?>", " ", content)
    content = re.sub(r"</font>"," ", content)
    content = re.sub(r"<font.*?>", " ", content)
    content = re.sub(r"<b>|</b>", " ", content)
    content = re.sub(r"<strong>|</strong>", " ", content)
    content = re.sub(r"<p>|</p>", " ", content)
    content = re.sub(r"&nbsp;"," ", content)
    content = re.sub(r"<!--.*?>", "", content)
    content = re.sub(r"<u>|</u>", "", content)
    return content

def comp_info_parser(content, comp_info):
    """
        解析公司信息
    """
    try:
        comp_name = re.findall(r"<div class=\"su_tit\">.*?</div>\s*<div class=\"su_con\">\s*<a title=.*?>(.*?)</a>|<div class=\"su_tit\">.*?</div>\s*<div class=\"su_con\">\s*(.*?)\s*<i class=\"picq qiye\" title=.*?></i>", content)
        if comp_name[0][1] == '':
            comp_name = comp_name[0][0]
        if comp_name[0][0] == '':
            comp_name = comp_name[0][1]
    except:
        comp_name = ' '

    try:
        side = re.findall(r"<b class=\"c_e50\">(.*?)\s*</li>\s*<li>\s*<i>.*?</i>\s*<b class=\"c_e50\">\s*(.*?)\s*</li>\s*<li>\s*<i>.*?</i>\s*(.*?)\s*</li>\s*<li>\s*<i>.*?</i>\s*(.*?)\s*</li>\s*<li>", content)
        regis_time = side[0][2]   #注册时间
        regis_address = side[0][3]   #注册地址
    except:
        regis_time = ' '   #注册时间
        regis_address = ' '   #注册地址

    comp_url =  re.findall(r"<div class=\"su_con\">\s*<a\stitle=\".*?\"\shref=\"(.*?)/\"\s*rel=\"nofollow\">", content)
    try:
        if len(comp_url) == 0 :
            comp_url = ""
        else:
            comp_url = comp_url[0]
    except:
        comp_url = ' '

    shop_url = re.findall(r"</ul>\s*<a href=\"(.*?)\/\?info.*?\"\sclass=\"goshop\"\sonClick=\"clickLog\s*.*?\">", content)
    if len(shop_url)==0:
        shop_url = ""
    else:
        shop_url = shop_url[0]

    comp_info_id = uuid.uuid4()
    comp_info['comp_info_id'] = comp_info_id
    comp_info['comp_name'] = comp_name
    try:
        regis_time = time.strptime(regis_time, "%Y.%m.%d")
        regis_time = datetime.datetime(* regis_time[:6])  #字符串转换成日期型
        comp_info['reg_time'] = regis_time
    except:
        comp_info['reg_time'] = datetime.datetime.now()

    comp_info['reg_address'] = regis_address
    comp_info['comp_url'] = comp_url
    comp_info['shop_url'] = shop_url

    return comp_info

def business_info_parser(content, business_info):
    """
     解析业务信息
    """
    try:
        business_name = re.findall(r"(?<=\<h1\>).*?(?=\<\/h1\>)", content)
        business_name = business_name[0]
    except:
        business_name = ' '

    try:
        business_released_data = re.findall(r"<li title=\".*?\" class=\"time\">(.*?)</li>", content)
        business_released_data = business_released_data[0]
    except:
        business_released_data = ' '

    try:
        link_people = re.findall(r"<div class=\"su_con\">\s*<a\starget=\"_blank\"\shref=\".*?\">(.*?)</a>\s*", content)
        link_people = link_people[0]
    except:
        link_people = ' '

    try:
        telephone = re.findall(r"<div class=\"su_con\">\s*<span id=\"t_phone\" class=\"phone tel\">(.*?)</span>|<div class=\"yyarea\">\s*<div class=\"p400\">\s*<span class=\"step\"></span>\s*<span\s*class=\"l_phone\">(.*?)<em></em></span>",content)
        if telephone[0][1] == '':
            telephone = telephone[0][0]
        if telephone[0][0] == '':
            telephone = telephone[0][1]
    except:
        telephone = ' '

    try:
        father_type = re.findall(r"<li><i class=\"z\"><nobr>.*?</nobr></i>\s*<a class=\".*?\">(.*?)</a>\s*</li>", content)
        father_type = father_type[0]
    except:
        father_type = ' '

    try:
        side = re.findall(r"<b class=\"c_e50\">(.*?)\s*</li>\s*<li>\s*<i>.*?</i>\s*<b class=\"c_e50\">\s*(.*?)\s*</li>\s*<li>\s*<i>.*?</i>\s*(.*?)\s*</li>\s*<li>\s*<i>.*?</i>\s*(.*?)\s*</li>\s*<li>", content)
        reservation_counts = side[0][1]    #预约次数
    except:
        reservation_counts = ' '    #预约次数

    try:
        view_counts = re.findall(r"<em\s*id=\"totalcount\">(.*?)</em>", content)
        view_counts = view_counts[0]
    except:
        view_counts = ' '

    try:
        child_type = re.findall(r"(<li><i class=\"z\"><nobr>.*?</nobr></i>\s*)?<a class=\"\" href=\".*?\" target=\"_blank\">(.*?)</a>\s*", content)
        temp = []
        for i in range(len(child_type)):
            str = child_type[i][1].encode('utf-8')
            temp.append(str)
        child_type = ','.join(temp)
    except:
        child_type = ' '

    business_info['business_name'] = business_name

    try:
        business_released_data = time.strptime(business_released_data, "%Y-%m-%d")
        business_released_data = datetime.datetime(* business_released_data[:6])
        business_info['business_released_date'] = business_released_data
    except:
        business_info['business_released_date'] = datetime.datetime.now()

    business_info['link_people'] = link_people
    business_info['telephone'] = telephone
    business_info['father_type'] = father_type
    try:
        reservation_counts = int(reservation_counts.encode('utf-8').split(' ')[0])
        business_info['reservation_counts'] = reservation_counts
    except:
        business_info['reservation_counts'] = 0

    try:
        business_info['view_counts'] = int(view_counts)
    except:
        business_info['view_counts'] = 0

    business_info['child_type'] = child_type

    return business_info


def business_detail_info_parser(content, business_detail_info):
    """
        业务详情描述解析
    """
    try:
        business_detail = re.findall(r"<div class=\"descriptionBox\">\s*<article\sclass=\"description_con\">\s*<span .*?>(.*?)</span>.*?</article>|<div class=\"descriptionBox\">\s*<article\sclass=\"description_con\">(.*?)</article>", content)
        if business_detail[0][1] == '':
            business_detail = business_detail[0][0]
        if business_detail[0][0] == '':
            business_detail = business_detail[0][1]
    except:
        business_detail = ' '

    business_detail_id = uuid.uuid4()
    business_detail_info['business_detail_id'] = business_detail_id
    business_detail_info['business_detail'] = business_detail

    return business_detail_info


def info_save(business_info, business_detail_info, comp_info):
    business_save(business_info, comp_info, business_detail_info)



