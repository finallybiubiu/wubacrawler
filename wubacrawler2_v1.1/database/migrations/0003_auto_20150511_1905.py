# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20150511_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='flag',
            field=models.IntegerField(default=0, max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='businessdetail',
            name='id',
            field=models.CharField(default=b'798d9cd5-aee5-439a-bbd8-10a96a2d46fd', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='businessinfo',
            name='id',
            field=models.CharField(default=b'c0ce3f70-09dc-4444-a7ef-41c7d73b2e00', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='id',
            field=models.CharField(default=b'dce0d885-4080-42db-a696-b2ca2a9b587f', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcecode',
            name='id',
            field=models.CharField(default=b'ab0d4153-3b0d-42b7-92ed-ba60468b133e', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sourcedetail',
            name='id',
            field=models.CharField(default=b'1f482acb-8963-412b-9905-26eb0f6a0a7c', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True),
            preserve_default=True,
        ),
    ]
