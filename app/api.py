
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.models import User
from ceshi import cfg
from libs.http import render_json

# Create your views here.
from app import scripts


def first_api(request):
    request.session['name'] = 'xxxx'
    avatar = request.FILES['avatar']
    request.set_cookie(avatar)
    return HttpResponse('hello first_api')



def render_html(request):
    request.session['name'] = 'xxxx'
    return render(request, 'index.html')


from app import cfhs, logics


def hello(request):
    cfhs.dddd.delay()
    return HttpResponse('hello')


def login(request):
    name = request.GET.get('name')
    User.objects.get_or_create(
        name=name,
    )
    return render_json()


def wb_authorize(request):
    # 授权回调页
    return redirect(cfg.WB_AUTH_URL)


def wb_callback(request):
    # 获取access_token,uid
    code = request.GET.get('code')
    access_token, uid = logics.get_access_token(code)
    # 获取用户信息
    user_info = logics.get_user_info(access_token, uid)
    if not user_info:
        return render_json(code=1001)
    # 执行登录
    # try:
    #     user = User.objects.get(name=user_info['name'])
    # except User.DoesNotExist:
    #     user = User.objects.create(**user_info)
    # TODO 和try 方法等价
    user, _ = User.objects.get_or_create(**user_info)
    # print(user)
    return render_json(user.to_dict())


def alipay_callback(request):
    pass


def alipay_authorize(request):
    return redirect()
def get_avatar(request):
    avatar = request.FILES.get('avatar')
    # print(avatar.__dict__,dir(avatar))
    # dir('对象') 列出对象的所有属性和方法
    scripts.avatar_download(avatar)
    return render_json()

