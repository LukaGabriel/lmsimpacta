# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_auto_20171112_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
