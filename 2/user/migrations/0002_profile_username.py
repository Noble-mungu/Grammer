# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-10 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
