from django.shortcuts import render
from django.core.paginator import *
from django.conf import settings
from .models import *
from haystack.views import SearchView
# 视图以通用视图实现
class MySearchView(SearchView):
    # 模版文件
    template = 'search.html'
    # 重写响应方式
    # 如果请求参数q为空，返回模型Product的全部数据
    # 否则根据参数q搜索相关数据
    def create_response(self):
        if not self.request.GET.get('q', ''):
            show_all = True
            product = Product.objects.all().order_by('id')
            per = settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE
            p = Paginator(product, per)
            try:
                num = int(self.request.GET.get('page', 1))
                page = p.page(num)
            except PageNotAnInteger:
                # 如果参数page不是整型，则返回第1页数据
                page = p.page(1)
            except EmptyPage:
                # 访问页数大于总页数，则返回最后1页的数据
                page = p.page(p.num_pages)
            return render(self.request, self.template, locals())
        else:
            show_all = False
            qs = super(MySearchView, self).create_response()
            return qs