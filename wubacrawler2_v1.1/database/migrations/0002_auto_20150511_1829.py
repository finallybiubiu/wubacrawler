# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessDetail',
            fields=[
                ('id', models.CharField(default=b'd9d424ad-0476-40f6-8254-63d6164a238c', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True)),
                ('business_detail', models.TextField(default=0, verbose_name='\u4e1a\u52a1\u8be6\u60c5\u63cf\u8ff0')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u8bb0\u5f55\u63d2\u5165\u65f6\u95f4')),
            ],
            options={
                'db_table': 'database_businessdetail',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.CharField(default=b'90767e77-1c3f-455b-ac4b-67b17dea8aea', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True)),
                ('business_name', models.CharField(max_length=100, verbose_name='\u4e1a\u52a1\u540d\u79f0')),
                ('business_released_date', models.DateField(verbose_name='\u4e1a\u52a1\u53d1\u5e03\u65e5\u671f')),
                ('link_people', models.CharField(max_length=50, verbose_name='\u4e1a\u52a1\u8054\u7cfb\u4eba')),
                ('telephone', models.CharField(max_length=50, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('father_type', models.CharField(max_length=40, null=True, verbose_name='\u4e1a\u52a1\u6240\u5c5e\u7c7b\u522b')),
                ('reservation_counts', models.IntegerField(null=True, verbose_name='\u9884\u7ea6\u6b21\u6570')),
                ('view_counts', models.IntegerField(null=True, verbose_name='\u4e3b\u9875\u6d4f\u89c8\u6b21\u6570')),
                ('child_type', models.CharField(max_length=100, verbose_name='\u5b50\u7c7b\u4fe1\u606f')),
                ('created_on', models.DateTimeField(verbose_name='\u8bb0\u5f55\u6dfb\u52a0\u65f6\u95f4')),
                ('business_detail', models.ForeignKey(to='database.BusinessDetail')),
            ],
            options={
                'db_table': 'database_businessinfo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.CharField(default=b'6d5bfee8-e71c-4725-901f-548b413eabeb', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True)),
                ('comp_name', models.CharField(max_length=100, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('reg_time', models.DateTimeField(verbose_name='\u6ce8\u518c\u65f6\u95f4')),
                ('reg_address', models.CharField(max_length=100, verbose_name='\u6ce8\u518c\u5730\u5740')),
                ('comp_url', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u5b98\u7f51')),
                ('shop_url', models.CharField(max_length=255, verbose_name='\u5e97\u94fa\u7f51\u5740')),
                ('created_on', models.DateTimeField(verbose_name='\u8bb0\u5f55\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'company_infomation',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='comp_name',
            field=models.ForeignKey(related_name='comp_business', to='database.CompanyInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='url',
            field=models.ForeignKey(to='database.SourceDetail'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcecode',
            name='id',
            field=models.CharField(default=b'fa246131-5aae-4830-a951-2bb15926fd33', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcecode',
            name='url',
            field=models.ForeignKey(to='database.SourceDetail'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcedetail',
            name='id',
            field=models.CharField(default=b'405c3c8f-b581-473a-9935-b41d9b8842be', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True),
            preserve_default=True,
        ),
    ]
