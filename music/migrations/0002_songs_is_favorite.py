# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-29 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
