# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
            ],
        ),
    ]