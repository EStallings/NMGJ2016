# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='url',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='game',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='turn_time',
            field=models.DurationField(),
        ),
    ]
