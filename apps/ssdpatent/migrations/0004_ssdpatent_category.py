# Generated by Django 2.0.1 on 2020-08-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssdpatent', '0003_remove_ssdpatent_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssdpatent',
            name='category',
            field=models.CharField(blank=True, choices=[('0', '未分类'), ('1', '太赫兹'), ('2', '遥感成像'), ('3', '高可靠嵌入式'), ('4', '智能识别'), ('5', '化学化工'), ('6', '新能源'), ('7', '机械'), ('8', '环保和资源'), ('9', '交通运输'), ('10', '橡胶塑料'), ('11', '仪器仪表'), ('12', '新型材料'), ('13', '电子信息'), ('14', '医药与医疗'), ('15', '农林牧业'), ('16', '海洋开发'), ('17', '航空航天'), ('18', '采矿治金'), ('19', '电气自动化'), ('20', '包装印刷'), ('21', '教育休闲'), ('22', '钒钛产业'), ('23', '安全防护')], default='0', max_length=3, null=True, verbose_name='行业分类'),
        ),
    ]