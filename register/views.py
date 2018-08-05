from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from forms import *
from models import *
import uuid
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse

# Create your views here.
def index(request):
    hashkey = CaptchaStore.generate_key()
    imgage_url = captcha_image_url(hashkey)
    data = {
        'hashkey': hashkey,
        'image_url': imgage_url,

    }
    # return HttpResponse(data['user_form'])
    return render(request,'regist/index.html',data)


def signup(request):
    register_form = UserForm(request.POST)
    if register_form.is_valid():
        user_name = request.POST.get('username','')
        pass_word = request.POST.get('password','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        user_id = uuid.uuid4()

        user = User()
        user.name = user_name
        user.user_id = user_id
        user.password = pass_word
        user.mobile = user.mobile
        user.email = user.email

        if user.save():
            return render(request,'/')

