# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20170926_1456'),
        ('cars_app', '0004_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='cars',
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='login_app.User'),
        ),
    ]