# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
