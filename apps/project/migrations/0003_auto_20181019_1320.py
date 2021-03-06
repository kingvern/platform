# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-19 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20181019_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='publish_time',
        ),
        migrations.AddField(
            model_name='project',
            name='bargain',
            field=models.BooleanField(default=False, verbose_name='\u8bae\u4ef7'),
        ),
        migrations.AddField(
            model_name='project',
            name='cooperation',
            field=models.CharField(choices=[('0', '\u80a1\u6743\u6295\u8d44'), ('1', '\u6280\u672f\u8f6c\u8ba9'), ('2', '\u8bb8\u53ef\u4f7f\u7528'), ('3', '\u5408\u4f5c\u5f00\u53d1'), ('4', '\u5408\u4f5c\u5174\u529e\u65b0\u4f01\u4e1a'), ('5', '\u5176\u4ed6')], default='0', max_length=100, verbose_name='\u9879\u76ee\u7c7b\u522b'),
        ),
        migrations.AddField(
            model_name='project',
            name='field_category',
            field=models.CharField(choices=[('0', '\u98df\u54c1\u996e\u6599'), ('1', '\u5efa\u7b51\u5efa\u6750'), ('2', '\u5bb6\u5c45\u7528\u54c1'), ('3', '\u8f7b\u5de5\u7eba\u7ec7'), ('4', '\u5316\u5b66\u5316\u5de5'), ('5', '\u65b0\u80fd\u6e90'), ('6', '\u673a\u68b0'), ('7', '\u73af\u4fdd\u548c\u8d44\u6e90'), ('8', '\u6a61\u80f6\u5851\u6599'), ('9', '\u4eea\u5668\u4eea\u8868'), ('10', '\u65b0\u578b\u6750\u6599'), ('11', '\u7535\u5b50\u4fe1\u606f'), ('12', '\u533b\u836f\u4e0e\u533b\u7597'), ('13', '\u519c\u6797\u7267\u4e1a'), ('14', '\u6d77\u6d0b\u5f00\u53d1'), ('15', '\u822a\u7a7a\u822a\u5929'), ('16', '\u91c7\u77ff\u51b6\u91d1'), ('17', '\u7535\u6c14\u81ea\u52a8\u5316'), ('18', '\u5305\u88c5\u5370\u5237'), ('19', '\u6559\u80b2\u4f11\u95f2'), ('20', '\u9492\u949b\u4ea7\u4e1a'), ('21', '\u5b89\u5168\u9632\u62a4'), ('22', '\u4ea4\u901a\u8fd0\u8f93')], default='0', max_length=100, verbose_name='\u6240\u5c5e\u884c\u4e1a'),
        ),
        migrations.AddField(
            model_name='project',
            name='hire',
            field=models.IntegerField(default=0, verbose_name='\u4f63\u91d1'),
        ),
        migrations.AddField(
            model_name='project',
            name='keyword',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5173\u952e\u8bcd'),
        ),
        migrations.AddField(
            model_name='project',
            name='main_pic',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='\u9879\u76ee\u4e3b\u56fe'),
        ),
        migrations.AddField(
            model_name='project',
            name='price',
            field=models.IntegerField(default=0, verbose_name='\u4ef7\u683c'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_category',
            field=models.CharField(choices=[('0', '\u672a\u77e5'), ('1', '\u5b9e\u9a8c\u5ba4\u9636\u6bb5'), ('2', '\u6837\u54c1\u9636\u6bb5'), ('3', '\u5c0f\u8bd5\u9636\u6bb5'), ('4', '\u4e2d\u8bd5\u9636\u6bb5'), ('5', '\u91cf\u4ea7\u9636\u6bb5')], default='0', max_length=100, verbose_name='\u9879\u76ee\u7c7b\u522b'),
        ),
        migrations.AddField(
            model_name='project',
            name='province',
            field=models.CharField(choices=[('bj', '\u5317\u4eac'), ('tj', '\u5929\u6d25')], default='bj', max_length=20, verbose_name='\u9879\u76ee\u6240\u5728\u5730\u533a'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('sqwjf', '\u6388\u6743\u672a\u7ed3\u8d39'), ('yxzs', '\u5df2\u4e0b\u8bc1\u4e66')], max_length=20, null=True, verbose_name='\u9879\u76ee\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='\u9879\u76ee\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='\u9879\u76ee\u540d'),
        ),
    ]
