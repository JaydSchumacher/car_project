# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='cars',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]