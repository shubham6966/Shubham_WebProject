# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 04:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NutritionManagement', '0004_auto_20170929_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 9, 30, 9, 44, 18, 712779)),
        ),
    ]
