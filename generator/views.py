from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    character = list('abcdefghijklmnopqrstuvwxyz')  # list will split the whole string into a single single character

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTVWXYZ'))

    if request.GET.get('number'):
        character.extend('1234567890')

    if request.GET.get('special'):
        character.extend('!@#$%^&*')

    c = ''
    if request.GET.get('specialChar'):
        c = request.GET.get('specialChar')

    length = int(request.GET.get('length', 12))  # just giving a initial value 12 if user does not provides any length
    the_password = ''

    if request.GET.get('specialCharatEnd'):
        for i in range(length):
            the_password += random.choice(character)
        the_password += c
    else:
        the_password = c
        for i in range(length):
            the_password += random.choice(character)

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')
