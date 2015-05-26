#-*- coding:utf-8 -*-

import uuid
import copy
import datetime
from django.db import models


class SourceDetail(models.Model):
    """源码细节表"""

    SOURCE_TYPE = (('1', 'Html'),
                   ('2', 'Json'))

    id = models.CharField(u'标识符', primary_key = True, default = str(uuid.uuid4()), max_length = 64)
    url = models.CharField(u'源码对应的url', max_length=255, null=True)
    url_md5 = models.CharField(u'md5加密后的url', max_length=40, null=True)
    source_type = models.CharField(u'源码类型', max_length=10, null=True, choices=SOURCE_TYPE)
    is_stable = models.BooleanField(u'源码内容是否变化', default = False)
    is_delete = models.BooleanField(u'源码内容是否被删除', default = False)
    created_on = models.DateTimeField(u'记录添加时间')

    class Meta:
        db_table = 'source_detail'

def source_detail_save(info):
    records = SourceDetail(id = str(uuid.uuid4()),
                           url = info['url'],
                           url_md5 = info['url_md5'],
                           source_type = 1,
                           created_on = datetime.datetime.now(),)
    records.save()
    return records


class SourceCode(models.Model):
    """html源码表"""
    id = models.CharField(u'标识符', primary_key = True, default = str(uuid.uuid4()), max_length = 64)
    url = models.ForeignKey(SourceDetail)
    source = models.TextField(u'页面源码内容', null= True)
    created_on = models.DateTimeField(u'记录添加时间')
    flag = models.IntegerField(default = 0)

    class Meta:
        db_table = 'source_code'


def source_code_save(source_code_info, source_detail_info):
    """源码信息表,源码细节表"""
    source_detail_info_2 = copy.deepcopy(source_detail_info)
    temp = SourceDetail.objects.filter(url = source_detail_info_2.pop('url'))
    if temp.exists():
        temp = temp[0]
    else:
        temp = source_detail_save(source_detail_info_2)

    records = SourceCode(id = str(uuid.uuid4()),
                         url = temp,
                         source = source_code_info['source'],
                         created_on = datetime.datetime.now())
    records.save()


class CompanyInfo(models.Model):

    id = models.CharField(u'标识符', primary_key=True, default = str(uuid.uuid4()), max_length=64)
    comp_name = models.CharField(u'公司名称', max_length = 100)
    reg_time = models.DateTimeField(u'注册时间')
    reg_address = models.CharField(u'注册地址', max_length = 1000)
    comp_url = models.CharField(u'公司官网', max_length = 255)
    shop_url = models.CharField(u'店铺网址', max_length = 255)
    created_on = models.DateTimeField(u'记录添加时间')

    class Meta:
        db_table = 'company_infomation'

def comp_save(info):
    records = CompanyInfo(id = str(uuid.uuid4()),
                          comp_name = info.pop('comp_name'),
                          reg_time = info.pop('reg_time'),
                          reg_address = info.pop('reg_address'),
                          comp_url = info.pop('comp_url'),
                          shop_url = info.pop('shop_url'),
                          created_on = datetime.datetime.now()
                          )
    records.save()
    return records


class BusinessDetail(models.Model):

    id = models.CharField(u'标识符', primary_key = True, default = str(uuid.uuid4()), max_length = 64)
    business_detail = models.TextField(u'业务详情描述',default = 0)
    created_on = models.DateTimeField(u'记录插入时间', auto_now_add = True)

    class Meta:
        db_table = 'database_businessdetail'

def business_detail_save(info):
    records = BusinessDetail(id = str(uuid.uuid4()),
                             business_detail = info.pop('business_detail'),
                             created_on = datetime.datetime.now())
    records.save()
    return records

class BusinessInfo(models.Model):

    id = models.CharField(u'标识符', primary_key = True, default = str(uuid.uuid4()), max_length = 64)
    url = models.ForeignKey(SourceDetail)
    business_name = models.CharField(u'业务名称', max_length = 100)
    business_detail = models.ForeignKey(BusinessDetail)
    business_released_date = models.DateField(u'业务发布日期')
    comp_name = models.ForeignKey(CompanyInfo, related_name = 'comp_business')
    link_people = models.CharField(u'业务联系人', max_length = 50)
    telephone = models.CharField(u'联系电话', max_length = 50)
    father_type = models.CharField(u'业务所属类别', max_length = 40, null = True)
    reservation_counts = models.IntegerField(u'预约次数', null = True)
    view_counts = models.IntegerField(u'主页浏览次数', null = True)
    child_type = models.CharField(u'子类信息', max_length = 100)
    created_on = models.DateTimeField(u'记录添加时间')
    flag = models.IntegerField(max_length=10,default = 0, null = True)

    class Meta:
        db_table = 'database_businessinfo'

def business_save(info, comp_info, business_detail_info):

    temp = CompanyInfo.objects.filter(id = str(comp_info['comp_info_id']))
    if temp.exists():
        temp = temp[0]
    else:
        temp = comp_save(comp_info)

    temp2 = BusinessDetail.objects.filter(id = str(business_detail_info['business_detail_id']))
    if temp2.exists():
        temp2 = temp2[0]
    else:
        temp2 = business_detail_save(business_detail_info)


    records = BusinessInfo(id = str(uuid.uuid4()),
                           url_id = info.pop('url_id'),
                           business_name = info.pop('business_name'),
                           business_released_date = info.pop('business_released_date'),
                           comp_name = temp,
                           business_detail = temp2,
                           link_people = info.pop('link_people'),
                           telephone = info.pop('telephone'),
                           father_type = info.pop('father_type'),
                           reservation_counts = info.pop('reservation_counts'),
                           view_counts = info.pop('view_counts'),
                           child_type = info.pop('child_type'),
                           created_on = datetime.datetime.now(),
                           flag = 0)
    records.save()


class WuBa(models.Model):
    """
        58同城汇总模型
    """
    id = models.CharField(u'标识符', primary_key=True, default = str(uuid.uuid4()), max_length=64)
    comp_name = models.CharField(u'公司名称', max_length = 100)
    reg_time = models.DateTimeField(u'注册时间')
    reg_address = models.CharField(u'注册地址', max_length = 1000)
    comp_url = models.CharField(u'公司官网', max_length = 255)
    shop_url = models.CharField(u'店铺网址', max_length = 255)
    source_url = models.CharField(u'来源网址', max_length = 255)
    source_url_mapping = models.CharField(u'来源网址md5加密', max_length = 255)
    business_name = models.CharField(u'业务名称', max_length = 100)
    business_released_date = models.DateField(u'业务发布日期')
    link_people = models.CharField(u'业务联系人', max_length = 50)
    telephone = models.CharField(u'联系电话', max_length = 50)
    father_type = models.CharField(u'业务所属类别', max_length = 40, null = True)
    reservation_counts = models.IntegerField(u'预约次数', null = True)
    view_counts = models.IntegerField(u'主页浏览次数', null = True)
    child_type = models.CharField(u'子类信息', max_length = 100)
    created_on = models.DateTimeField(u'记录添加时间')
    flag = models.IntegerField(default = 0, null = True)
    business_detail_id = models.CharField(u'业务详情描述', max_length = 64)
    comp_name_id = models.CharField(u'公司信息', max_length = 64)
    url_id = models.CharField(u'源码细节表', max_length = 64)


    class Meta:
        db_table = "wuba_loan"


def wuba_info_save(wuba_info):
    wb = WuBa()
    wb.id = wuba_info.get('id')
    wb.comp_name = wuba_info.get('comp_name', '')
    wb.reg_time = wuba_info.get('reg_time', '')
    wb.reg_address = wuba_info.get('reg_time', '')
    wb.comp_url = wuba_info.get('comp_url', '')
    wb.shop_url = wuba_info.get('shop_url', '')
    wb.source_url = wuba_info.get('source_url', '')
    wb.source_url_mapping = wuba_info.get('source_url_mapping', '')
    wb.business_name = wuba_info.get('business_name', '')
    wb.business_released_date = wuba_info.get('business_released_date', '')
    wb.link_people = wuba_info.get('link_people', '')
    wb.telephone = wuba_info.get('telephone', '')
    wb.father_type = wuba_info.get('father_type', '')
    wb.reservation_counts = wuba_info.get('reservation_counts', '')
    wb.view_counts = wuba_info.get('view_counts', '')
    wb.child_type = wuba_info.get('child_type', '')
    wb.created_on = datetime.datetime.now()
    wb.flag = 0
    wb.business_detail_id = wuba_info.get('business_detail_id', '')
    wb.comp_name_id = wuba_info.get('comp_name_id', '')
    wb.url_id = wuba_info.get('url_id', '')

    wb.save(using='saveinfo')


