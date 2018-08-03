# encoding:utf-8

from django.db import models

# Create your models here.
class User(models.Model):

    id = models.AutoField(primary_key=True) # 主键
    name = models.CharField(max_length = 20) # 用户名
    password = models.CharField(max_length = 20) # 密码
    email = models.CharField(max_length = 20) #邮箱
    mobile = models.CharField(max_length = 11) # 手机
    verifyCode = models.CharField(max_length = 20) # 验证码
    loginTime = models.DateField() # 登录时间
    registTime = models.DateField() #注册时间
