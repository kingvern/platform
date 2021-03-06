# _*_ coding: utf-8 _*_


import xadmin

from .models import UserAsk, UserFavorite, UserMessage, BuyerPatent, BuyerProject

from datetime import datetime


class UserAskAdmin(object):
    list_display = ['user', 'add_time']
    search_fields = ['user', ]
    list_filter = ['user', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


# 卖家 业务员 合同 资料(业务员上传) 业务员接收
class BuyerPatentAdmin(object):
    list_display = ['id', 'patent', 'get_seller_username', 'get_seller_mobile', 'buyer', 'total_price', 'step', 'staff']
    search_fields = ['id', 'patent', 'buyer', 'total_price', 'step']
    list_filter = ['id', 'patent', 'buyer', 'total_price', 'step']
    refresh_times = [3, 5]
    relfield_style = 'fk-ajax'
    list_editable = ['step', 'staff']

    # def save_models(self):
    #     #  在保存课程的时候统计课程机构的课程数
    #     obj = self.new_obj
    #     obj.step_time = datetime.now()
    #     obj.save()
    #     if obj.step == '-1':
    #         patent = obj.patent
    #         patent.shop_status = 1
    #         patent.save()
    #     if obj.step in ['0', '1', '2']:
    #         patent = obj.patent
    #         patent.shop_status = 2
    #         patent.save()
    #     if obj.step == '3':
    #         patent = obj.patent
    #         patent.shop_status = 3
    #         patent.save()


# 卖家 业务员 合同 资料(业务员上传) 业务员接收
class BuyerProjectAdmin(object):
    list_display = ['id', 'project', 'get_seller_username', 'get_seller_mobile', 'buyer', 'step', 'contract', 'prof',
                    'protocol', 'staff']
    search_fields = ['id', 'project', 'buyer', 'step', 'contract', 'prof',
                     'protocol']
    list_filter = ['id', 'project', 'buyer', 'step', 'contract', 'prof',
                   'protocol']
    refresh_times = [3, 5]
    relfield_style = 'fk-ajax'
    list_editable = ['step', 'contract', 'prof', 'protocol','staff']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(BuyerPatent, BuyerPatentAdmin)
xadmin.site.register(BuyerProject, BuyerProjectAdmin)
