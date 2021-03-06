# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-22 12:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0004_remove_policy_add_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name': '\u884c\u653f\u7ea7\u522b', 'verbose_name_plural': '\u884c\u653f\u7ea7\u522b'},
        ),
        migrations.RemoveField(
            model_name='department',
            name='Province',
        ),
        migrations.AddField(
            model_name='department',
            name='if_show',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a'),
        ),
        migrations.AddField(
            model_name='policy',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AddField(
            model_name='province',
            name='if_show',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.Province', verbose_name='\u6240\u5c5e\u884c\u653f'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policy.Department', verbose_name='\u6240\u5c5e\u90e8\u95e8'),
        ),
    ]
