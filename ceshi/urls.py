"""ceshi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import api as app_api
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^ceshi/app/first_api',app_api.first_api),
    url(r'^ceshi/app/render_html',app_api.render_html),
    url(r'^ceshi/app/hello',app_api.hello),
    url(r'^ceshi/app/login',app_api.login),
    url(r'^wb_authorized',app_api.wb_authorize),
    url(r'ceshi/app/wb_callback',app_api.wb_callback),
    url(r'^alipay_authorized',app_api.alipay_authorize),
    url(r'^alipay/callback',app_api.alipay_callback)
]
