# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-21 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0002_banner_chart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policy',
            old_name='detail',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='policy',
            old_name='publish_time',
            new_name='pubDate',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='Province',
        ),
        migrations.RemoveField(
            model_name='policy',
            name='name',
        ),
        migrations.AddField(
            model_name='policy',
            name='addr',
            field=models.CharField(default='', max_length=20, verbose_name='\u6240\u5c5e\u884c\u653f'),
        ),
        migrations.AddField(
            model_name='policy',
            name='policy_id',
            field=models.CharField(default='', max_length=20, verbose_name='\u653f\u7b56ID'),
        ),
        migrations.AddField(
            model_name='policy',
            name='source',
            field=models.CharField(default='', max_length=20, verbose_name='\u6240\u5c5e\u90e8\u95e8'),
        ),
        migrations.AddField(
            model_name='policy',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='\u653f\u7b56\u540d'),
        ),
    ]