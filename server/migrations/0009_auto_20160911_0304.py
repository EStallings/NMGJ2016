# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 03:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20160911_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 3, 4, 12, 425393)),
        ),
        migrations.AlterField(
            model_name='player',
            name='active',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 3, 4, 12, 433974)),
        ),
    ]
