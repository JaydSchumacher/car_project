# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.

# index --> '/'
def index(request):
    #User.objects.all().delete()
    return render(request, 'login_app/login.html')

def logout(request):
    request.session.flush()
    return redirect('/')

# login --> ('/login')
def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, 'Email or password not correct')
        return redirect('/')
    request.session['email'] = results['user'].email
    request.session['first_name'] = results['user'].first_name
    request.session['curUser'] = results['user'].id
   
    return redirect('/dashboard')

# register --> '/register$'
def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, 'You have been registered')
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')

def userprofile(request, id):
    context = {
        'user' : User.objects.get(id = id)
    }
    return render(request, 'login_app/profile.html')
