# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    name = forms.CharField(max_length = 20) # 用户名
    password = forms.CharField(max_length = 20) # 密码
    email = forms.EmailField(max_length = 20) #邮箱
    mobile = forms.CharField(max_length = 11) # 手机
    verifyCode = CaptchaField(error_messages={'invalid':'验证码有误'}) # 验证码

