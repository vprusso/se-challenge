# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-23 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
