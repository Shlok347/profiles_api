# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-05 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0005_userprofile_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]