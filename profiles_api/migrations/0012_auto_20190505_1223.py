# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-05 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0011_auto_20190505_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='imei',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_password',
            field=models.CharField(default=1111, max_length=254),
            preserve_default=False,
        ),
    ]
