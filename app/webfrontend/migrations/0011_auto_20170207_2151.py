# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webfrontend', '0010_auto_20170207_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slackmessage',
            old_name='tz',
            new_name='ts',
        ),
    ]
