# Generated by Django 2.2 on 2019-04-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=100)),
                ('live', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '个人信息表',
                'db_table': 'personinfo',
            },
        ),
    ]
