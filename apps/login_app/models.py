# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re


# Create your models here.

class UserManager(models.Manager):
    def creator(self, postData):
        user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password= bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user

    def loginVal(self, postData):
        results = {'status': True, 'errors':[], 'user': None}
        users = self.filter(email = postData['email'])
        
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] =  users[0]
            else:
                results['status'] = False
        return results

    def validate(self, postData):
        results = {'status': True, 'errors':[]}

        if len(postData['first_name']) < 3:
            results['errors'].append('First name too short')
            results['status'] = False
        if postData['first_name'] ==  '  ':
            results['errors'].append('First name not valid')
            results['status'] = False
        if len(postData['last_name']) < 3:
            results['errors'].append('Last name too short')
            results['status'] = False
        if postData['last_name'] ==  '   ':
            results['errors'].append('Last name not valid')
            results['status'] = False
        if not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', postData['email']):
            results['errors'].append('Email not valid')
            results['status'] = False
        if postData['password'] != postData['c_password']:
            results['errors'].append('Passwords does not match')
            results['status'] = False
        if len(postData['password']) < 5:
            results['errors'].append('Passwords must be at least 5 characters')
            results['status'] = False
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('User already exists')
            results['status'] = False
        
        return results
        

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()

