# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20160910_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='secret',
            field=models.CharField(default='no secret', max_length=200),
            preserve_default=False,
        ),
    ]