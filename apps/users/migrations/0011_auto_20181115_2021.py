# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-15 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20181101_1612'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailVerifyRecord',
        ),
        migrations.AlterModelOptions(
            name='updatemobilerecord',
            options={'verbose_name': '\u624b\u673a\u66f4\u65b0\u8bb0\u5f55', 'verbose_name_plural': '\u624b\u673a\u66f4\u65b0\u8bb0\u5f55'},
        ),
    ]