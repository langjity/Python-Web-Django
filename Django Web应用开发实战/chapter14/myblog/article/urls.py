"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    # 首页地址自动跳转用户登录页面
    path('', RedirectView.as_view(url='user/login.html')),
    # 文章列表
    path('<int:id>/<int:page>.html', article, name='article'),
    # 文章正文内容
    path('detail/<int:id>/<int:aId>.html', detail, name='detail')
]
