from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first_api(request):
    return HttpResponse('hello first_api')
