# Generated by Django 2.0.1 on 2019-01-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0016_auto_20181116_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='if_show',
            field=models.BooleanField(default=False, verbose_name='是否显示'),
        ),
    ]