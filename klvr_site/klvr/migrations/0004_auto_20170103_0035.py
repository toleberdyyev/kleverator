# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('klvr', '0003_auto_20170103_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_date',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
