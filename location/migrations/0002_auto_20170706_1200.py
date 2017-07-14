# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loc',
            name='lat',
            field=models.DecimalField(decimal_places=10, max_digits=11),
        ),
        migrations.AlterField(
            model_name='loc',
            name='lon',
            field=models.DecimalField(decimal_places=10, max_digits=11),
        ),
    ]
