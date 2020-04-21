from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from app import scripts


def first_api(request):
    return HttpResponse('hello first_api')
def get_avatar(request):
    avatar = request.FILES.get('avatar')
    # print(avatar.__dict__,dir(avatar))
    # dir('对象') 列出对象的所有属性和方法
    scripts.avatar_download(avatar)
    return JsonResponse({'code':100})