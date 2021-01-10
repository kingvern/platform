# Generated by Django 2.0.1 on 2020-08-18 20:36

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='头条名')),
                ('pic', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='头条主图')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='详情')),
                ('if_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击次数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏次数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加日期')),
            ],
            options={
                'verbose_name': '头条',
                'verbose_name_plural': '头条',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='成员名')),
                ('field', models.CharField(default='', max_length=100, verbose_name='行业领域')),
                ('logo', models.ImageField(blank=True, default='image/default.png', upload_to='image/%Y/%m', verbose_name='logo')),
                ('status', models.CharField(choices=[('-1', '驳回'), ('0', '审核中'), ('1', '通过审核')], default='1', max_length=20, verbose_name='审核状态')),
                ('note', models.CharField(blank=True, default='1', max_length=20, null=True, verbose_name='审核意见')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加日期')),
            ],
            options={
                'verbose_name': '成员管理',
                'verbose_name_plural': '成员管理',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='资源名')),
                ('download', models.FileField(upload_to='club/resource/%Y/%m', verbose_name='资源文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '资源',
                'verbose_name_plural': '资源',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='分节标题')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='详情')),
                ('if_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击次数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏次数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加日期')),
            ],
            options={
                'verbose_name': '分节',
                'verbose_name_plural': '分节',
            },
        ),
    ]