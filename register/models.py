# encoding:utf-8

from django.db import models

# Create your models here.
class User(models.Model):

    user_id = models.CharField(max_length=20,primary_key=True) #用户唯一编码
    name = models.CharField(max_length = 20) # 用户名
    password = models.CharField(max_length = 20) # 密码
    email = models.CharField(max_length = 20) #邮箱
    mobile = models.CharField(max_length = 11) # 手机
    loginTime = models.DateField() # 登录时间
    registTime = models.DateField() #注册时间
