# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20160616_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='image',
            new_name='poster',
        ),
    ]
