# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from ssdpatent.models import SSDPatent
from users.models import UserProfile
from patent.models import Patent
from project.models import Project


# Create your models here.

class UserAsk(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户', null=True)
    fav_id = models.IntegerField(default=0, verbose_name=u'数据ID')
    fav_type = models.IntegerField(choices=((0, u'政策'), (1, u'专利'), (2, u'项目'), (3, u'其他慢慢加')), default=1,
                                   verbose_name=u'数据类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据ID')
    fav_type = models.IntegerField(
        choices=((0, u'政策'), (1, u'专利'), (2, u'项目'), (3, u'孵化器'), (4, u'科技园区'), (5, u'金融机构'), (6, u'展会'), (7, u'展会点赞')),
        default=1,
        verbose_name=u'数据类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserJoin(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    join_id = models.IntegerField(default=0, verbose_name=u'数据ID')
    join_type = models.IntegerField(choices=((0, u'政策'), (1, u'专利'), (2, u'项目'), (3, u'展会')), default=1,
                                    verbose_name=u'数据类别')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户报名'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'接收用户')
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class BuyerPatent(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'买家',
                              related_name='patent_buyer_set')
    order_name = models.CharField(max_length=100, default='', verbose_name=u'单位名称')
    order_address = models.CharField(max_length=100, default='', verbose_name=u'地址')
    order_contact = models.CharField(max_length=100, default='', verbose_name=u'联系人')
    order_mobile = models.CharField(max_length=11, default='', verbose_name=u'手机')
    patent = models.ForeignKey(SSDPatent, on_delete=models.CASCADE, verbose_name=u'专利')
    base_price = models.IntegerField(default=0, verbose_name=u'基础费')
    serve_fee = models.IntegerField(default=0, verbose_name=u'服务费')
    total_price = models.IntegerField(default=0, verbose_name=u'总费')
    step = models.CharField(max_length=10, default='0',
                            choices=(('-1', u'已取消'), ('0', u'下单未付款'), ('1', u'买家已付款'), ('2', u'已提交专利局'), ('3', u'交易完成')),
                            verbose_name=u'订单阶段')
    contract = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"合同",
        default='',
        null=True,
        blank=True,
        max_length=100)
    prof = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"付款凭证",
        default='', null=True,
        blank=True,
        max_length=100)
    step_time = models.DateTimeField(default=datetime.now, verbose_name=u'阶段时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, verbose_name=u'业务员',
                              related_name='patent_staff_set')

    def get_seller_username(self):
        return self.patent.asc

    get_seller_username.short_description = "专利权人"

    def get_seller_mobile(self):
        return self.patent.inc

    get_seller_mobile.short_description = "发明人"

    class Meta:
        verbose_name = '专利交易管理'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        # SSDPatent shop_status ('-1', u'已下架'), ('0', u'审核中'), ('1', u'已上架'), ('2', u'交易中'), ('3', u'已交易')
        # BuyerPatent step ('-1', u'已取消'), ('0', u'下单未付款'), ('1', u'买家已付款'), ('2', u'已提交专利局'), ('3', u'交易完成')
        self.step_time = datetime.now()
        if self.step == '-1':
            patent = self.patent
            patent.shop_status = '1'
            patent.save()
        if self.step in ['0', '1', '2']:
            patent = self.patent
            patent.shop_status = '2'
            patent.save()
        if self.step == '3':
            patent = self.patent
            patent.shop_status = '3'
            patent.save()


        # if self.step == '3':
        #     patent = self.patent
        #     patent.shop_status = '2'
        #     patent.save()

        super(self.__class__, self).save(*args, **kwargs)


class BuyerProject(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'买家',
                              related_name='project_buyer_set')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=u'项目')
    step = models.CharField(max_length=10, default='0', choices=(
        ('0', u'等待支付定金'), ('1', u'平台合同签订'), ('2', u'三方协议签订'), ('3', u'履约完成'), ('-1', u'取消或终止')),
                            verbose_name=u'订单阶段')
    step_time = models.DateTimeField(default=datetime.now, verbose_name=u'阶段时间')
    contract = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"合同",
        default='', null=True,
        blank=True,
        max_length=100)
    prof = models.FileField(
        upload_to="contract/resource/%Y/%m",
        verbose_name=u"定金凭证",
        default='', null=True,
        blank=True,
        max_length=100)
    protocol = models.FileField(
        upload_to="protocol/resource/%Y/%m",
        verbose_name=u"协议",
        default='', null=True,
        blank=True,
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, verbose_name=u'业务员',
                              related_name='project_staff_set')

    def get_seller_username(self):
        return self.project.seller.username

    get_seller_username.short_description = "卖家名字"

    def get_seller_mobile(self):
        return self.project.seller.mobile

    get_seller_mobile.short_description = "卖家手机号"

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.step_time = datetime.now()
    # 有毒

    class Meta:
        verbose_name = '技术项目订单管理'
        verbose_name_plural = verbose_name

class PatentComments(models.Model):
    # 会涉及两个外键: 1. 用户， 2. 专利。import进来
    patent = models.ForeignKey(SSDPatent, on_delete=models.CASCADE, verbose_name=u"专利")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    comments = models.CharField(max_length=250, verbose_name=u"评论", default='', null=True, blank=True)
    contact_name = models.CharField(max_length=250, verbose_name=u"联系人名字", default='', null=True, blank=True)
    contact_phone = models.CharField(max_length=250, verbose_name=u"联系人电话", default='', null=True, blank=True)
    budget = models.IntegerField(default=0, verbose_name=u"预算",  null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"专利评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对于《{1}》 评论 :'.format(self.user, self.patent)


class MessageBoard(models.Model):
    # 会涉及1个外键: 1. 用户
    patent_name = models.CharField(max_length=250, verbose_name=u"专利名")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户", default='', null=True, blank=True)
    comments = models.TextField(max_length=250, verbose_name=u"评论", default='', null=True, blank=True)
    contact_name = models.CharField(max_length=250, verbose_name=u"联系人名字", default='', null=True, blank=True)
    contact_phone = models.CharField(max_length=250, verbose_name=u"联系人电话", default='', null=True, blank=True)
    budget = models.IntegerField(default=0, verbose_name=u"预算", null=True, blank=True)
    category = models.CharField(max_length=3,
                                choices=(('0', '未分类'), ('1', '太赫兹'), ('2', '遥感成像'), ('3', '高可靠嵌入式'), ('4', '智能识别'),
                                         ('5', '化学化工'), ('6', '新能源'), ('7', '机械'), ('8', '环保和资源'), ('9', '交通运输'),
                                         ('21', '教育'), ('11', '仪器仪表'), ('12', '新型材料'), ('13', '电子信息'),
                                         ('14', '生物科学'), ('15', '农林牧业'),
                                         ('19', '电气自动化'),
                                         ('23', '安全防护')), default='0',
                                verbose_name=u'行业分类', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"留言板"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对于《{1}》 评论 :'.format(self.user, self.patent)
