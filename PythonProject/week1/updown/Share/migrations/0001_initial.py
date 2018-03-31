# Generated by Django 2.0.3 on 2018-03-31 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DownloadDocount', models.IntegerField(default=0, verbose_name='访问次数')),
                ('code', models.CharField(max_length=8, verbose_name='code')),
                ('Datatime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('path', models.CharField(max_length=32, verbose_name='下载路径')),
                ('name', models.CharField(default='', max_length=32, verbose_name='文件名')),
                ('Filesize', models.CharField(max_length=10, verbose_name='文件大小')),
                ('PCIP', models.CharField(default='', max_length=32, verbose_name='IP地址')),
            ],
            options={
                'verbose_name': 'download',
                'db_table': 'download',
            },
        ),
    ]
