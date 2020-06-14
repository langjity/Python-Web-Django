from django.contrib import admin
from .models import *

admin.site.site_title = 'MyDjango后台管理'
admin.site.site_header = 'MyDjango'


@admin.register(PersonInfo)
class PersonInfoAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'name', 'age']


@admin.register(Vocation)
class VocationAdmin(admin.ModelAdmin):
    # 在数据列表页设置显示的模型字段
    list_display = ['id', 'job', 'title', 'payment']

    # 重写get_readonly_fields函数
    # 设置超级管理员和普通用户的权限
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['payment']
        return self.readonly_fields

    # 在属性list_display中添加自定义字段colored_name
    # colored_name来自于模型Vocation
    list_display.append('colored_name')

    # 根据当前用户名设置数据访问权限
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id__lt=2)

    # 新增或修改数据时，设置外键可选值
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'person':
            if not request.user.is_superuser:
                v = Vocation.objects.filter(id__lt=2)
                kwargs['queryset'] = PersonInfo.objects.filter(id__in=v)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # 新增或修改数据时，设置下拉框的可选值
    # 为模型字段job新增下拉值“网页设计”
    # db_field.choices获取模型字段的属性choices的值
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'job':
            kwargs['choices'] = db_field.choices
            kwargs['choices'] += (('网页设计', '网页设计'),)
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    # 修改保存方法
    def save_model(self, request, obj, form, change):
        if change:
            # 获取当前用户名
            user = request.user.username
            # 使用模型获取数据，pk代表具有主键属性的字段
            job = self.model.objects.get(pk=obj.pk).job
            # 使用表单获取数据
            person = form.cleaned_data['person'].name
            # 写入日志文件
            f = open('d://log.txt', 'a')
            f.write(person + '职位：' + job + '，被' + user + '修改' + '\r\n')
            f.close()
        else:
            pass
        # 使用super在继承父类已有的功能下新增自定义功能
        super().save_model(request, obj, form, change)

    # 数据批量操作
    def get_datas(self, request, queryset):
        temp = []
        for d in queryset:
            t = [d.job, d.title, str(d.payment), d.person.name]
            temp.append(t)
        f = open('d://data.txt', 'a')
        for t in temp:
            f.write(','.join(t) + '\r\n')
        f.close()
        # 设置提示信息
        self.message_user(request, '数据导出成功！')

    # 设置函数的显示名称
    get_datas.short_description = '导出所选数据'
    # 添加到“动作”栏
    actions = ['get_datas']
