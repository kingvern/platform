# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-19 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20181019_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyerproject',
            old_name='user',
            new_name='buyer',
        ),
        migrations.AddField(
            model_name='buyerproject',
            name='contract',
            field=models.FileField(default='', upload_to='contract/resource/%Y/%m', verbose_name='\u5408\u540c'),
        ),
        migrations.AddField(
            model_name='buyerproject',
            name='protocol',
            field=models.FileField(default='', upload_to='protocol/resource/%Y/%m', verbose_name='\u534f\u8bae'),
        ),
    ]
