# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-08 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0004_auto_20181106_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financial',
            old_name='service',
            new_name='services',
        ),
        migrations.RemoveField(
            model_name='couveuse',
            name='gen_firm',
        ),
        migrations.RemoveField(
            model_name='park',
            name='service',
        ),
        migrations.AddField(
            model_name='couveuse',
            name='companys',
            field=models.TextField(blank=True, null=True, verbose_name='\u5b75\u5316\u4f01\u4e1a'),
        ),
        migrations.AddField(
            model_name='financial',
            name='url_introduce',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4ecb\u7ecd\u94fe\u63a5'),
        ),
        migrations.AddField(
            model_name='financial',
            name='url_services',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u670d\u52a1\u94fe\u63a5'),
        ),
        migrations.AddField(
            model_name='park',
            name='techservice',
            field=models.TextField(blank=True, null=True, verbose_name='\u670d\u52a1'),
        ),
        migrations.AddField(
            model_name='park',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='park',
            name='url_introduce',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4ecb\u7ecd\u94fe\u63a5'),
        ),
        migrations.AddField(
            model_name='park',
            name='url_techservice',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u670d\u52a1\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='couveuse',
            name='area1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u6240\u5728\u57301'),
        ),
        migrations.AlterField(
            model_name='couveuse',
            name='url_companys',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5b75\u5316\u4f01\u4e1a\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='couveuse',
            name='url_introduce',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4ecb\u7ecd\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='financial',
            name='area1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u6240\u5728\u57301'),
        ),
        migrations.AlterField(
            model_name='park',
            name='area1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u6240\u5728\u57301'),
        ),
    ]
