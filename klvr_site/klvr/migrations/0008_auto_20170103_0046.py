# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klvr', '0007_auto_20170103_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
