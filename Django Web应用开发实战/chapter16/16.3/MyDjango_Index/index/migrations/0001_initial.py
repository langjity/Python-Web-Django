# Generated by Django 2.2.1 on 2019-06-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('user', models.IntegerField()),
            ],
        ),
    ]
