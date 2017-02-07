# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_slack_oauth', '0005_auto_20161228_2055'),
        ('webfrontend', '0008_auto_20170206_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlackMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(db_index=True, max_length=20)),
                ('ts', models.DateTimeField()),
                ('type', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('data', models.TextField()),
                ('has_attachments', models.BooleanField(default=False)),
                ('edited', models.BooleanField(default=False)),
                ('my_slack_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webfrontend.MySlackUser')),
                ('slack_user_access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_slack_oauth.SlackUser')),
            ],
        ),
    ]