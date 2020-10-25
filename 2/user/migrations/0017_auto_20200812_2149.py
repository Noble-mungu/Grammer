# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-12 18:49
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]