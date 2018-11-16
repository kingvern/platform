# # _*_ coding: utf-8 _*_
#
# from django.core.mail import send_mail
#
# from random import Random
#
# from users.models import EmailVerifyRecord
# from platorm.settings import EMAIL_FROM
#
#
# def random_str(randomLength=8):
#     str = ''
#     chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
#     length = len(chars) - 1
#     random = Random()
#     for i in range(randomLength):
#         str += chars[random.randint(0, length)]
#     return str
#
#
# def send_register_email(email, send_type='register'):
#     email_record = EmailVerifyRecord()
#     code = random_str(16)
#     email_record.code = code
#     email_record.email = email
#     email_record.send_type = send_type
#     email_record.save()
#
#     email_title = ''
#     email_body = ''
#
#     if send_type == 'register':
#         email_title = '注册激活邮件'
#         email_body = '点击链接： http://127.0.0.1:8000/active/{0}/'.format(code)
#         send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
#         if send_status:
#             pass
#     elif send_type=='reset_pwd':
#         email_title = '密码重置邮件'
#         email_body = '点击链接： http://127.0.0.1:8000/reset/{0}/'.format(code)
#         send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
#         if send_status:
#             pass
#
