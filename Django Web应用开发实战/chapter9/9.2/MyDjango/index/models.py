from django.db import models

# Create your models here.
class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '人员信息'

class Vocation(models.Model):
    JOB = (
        ('软件开发', '软件开发'),
        ('软件测试', '软件测试'),
        ('需求分析', '需求分析'),
        ('项目管理', '项目管理'),
    )
    id = models.AutoField(primary_key=True)
    job = models.CharField(max_length=20, choices=JOB)
    title = models.CharField(max_length=20)
    payment = models.IntegerField(null=True, blank=True)
    person = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)
    recordTime = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '职业信息'
