# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length = 255)
    car_model = models.CharField(max_length = 255)
    year = models.IntegerField(default = 0000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    driver = models.ForeignKey(User, related_name = 'cars', null = True)