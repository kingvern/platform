# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-28 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userask',
            name='mobile',
            field=models.CharField(default='11111111111', max_length=11, verbose_name='\u624b\u673a'),
            preserve_default=False,
        ),
    ]