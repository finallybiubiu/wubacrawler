# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourceCode',
            fields=[
                ('id', models.CharField(default=b'ec5c1040-32f4-4854-908c-d479cea32cde', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True)),
                ('source', models.TextField(null=True, verbose_name='\u9875\u9762\u6e90\u7801\u5185\u5bb9')),
                ('created_on', models.DateTimeField(verbose_name='\u8bb0\u5f55\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'source_code',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceDetail',
            fields=[
                ('id', models.CharField(default=b'9f004c11-6c31-4fec-abc5-a1aef067d85c', max_length=64, serialize=False, verbose_name='\u6807\u8bc6\u7b26', primary_key=True)),
                ('url', models.CharField(max_length=255, null=True, verbose_name='\u6e90\u7801\u5bf9\u5e94\u7684url')),
                ('url_md5', models.CharField(max_length=40, null=True, verbose_name='md5\u52a0\u5bc6\u540e\u7684url')),
                ('source_type', models.CharField(max_length=10, null=True, verbose_name='\u6e90\u7801\u7c7b\u578b', choices=[(b'1', b'Html'), (b'2', b'Json')])),
                ('is_stable', models.BooleanField(default=False, verbose_name='\u6e90\u7801\u5185\u5bb9\u662f\u5426\u53d8\u5316')),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u6e90\u7801\u5185\u5bb9\u662f\u5426\u88ab\u5220\u9664')),
                ('created_on', models.DateTimeField(verbose_name='\u8bb0\u5f55\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'source_detail',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sourcecode',
            name='url',
            field=models.ForeignKey(related_name='source_record', to='database.SourceDetail'),
            preserve_default=True,
        ),
    ]
