# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-12 10:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200811_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
    ]