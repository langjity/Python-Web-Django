from django.urls import path
from .views import *

urlpatterns = [
    # 定义路由
    path('', index, name='index'),
    path('trunTo', trunTo.as_view(), name='trunTo')
]
