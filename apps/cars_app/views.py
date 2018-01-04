# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User, Car
from django.contrib import messages

# Create your views here.

def dashboard(request):

    context = {
        'user' : request.session['first_name'],
        'curUser': User.objects.get(id = request.session['curUser']),
        'otherUser': User.objects.all().exclude(id = request.session['curUser'])
    }
    if 'email' not in request.session:
        return redirect('/')
    return render(request, 'cars_app/dashboard.html', context)

def addcar(request):
    return render(request, 'cars_app/newcar.html')

def create(request):
    # print Car.objects.all()
    newCar = Car.objects.create(car_brand = request.POST['make'], car_model = request.POST['model'], year = request.POST['year'], driver =  User.objects.get(id = request.session['curUser']))
    return redirect('/dashboard')
    