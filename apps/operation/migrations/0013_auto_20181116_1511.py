# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-16 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0012_auto_20181116_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyerproject',
            options={'verbose_name': '\u6280\u672f\u9879\u76ee\u8ba2\u5355\u7ba1\u7406', 'verbose_name_plural': '\u6280\u672f\u9879\u76ee\u8ba2\u5355\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='buyerpatent',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patent_staff_set', to=settings.AUTH_USER_MODEL, verbose_name='\u4e1a\u52a1\u5458'),
        ),
        migrations.AddField(
            model_name='buyerproject',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_staff_set', to=settings.AUTH_USER_MODEL, verbose_name='\u4e1a\u52a1\u5458'),
        ),
        migrations.AlterField(
            model_name='buyerpatent',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patent_buyer_set', to=settings.AUTH_USER_MODEL, verbose_name='\u4e70\u5bb6'),
        ),
        migrations.AlterField(
            model_name='buyerproject',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_buyer_set', to=settings.AUTH_USER_MODEL, verbose_name='\u4e70\u5bb6'),
        ),
    ]
