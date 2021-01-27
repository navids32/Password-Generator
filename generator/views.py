from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
  return render(request, 'generator/home.html')

def about(request):
      return render(request, 'generator/about.html')

def password(request):
      
  characters = list('abcdefghiklmnopqrstuvwxyz')   
  if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIKLMNOPQRSTUVWXYZ'))
  if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+|'))
  if request.GET.get('numbers'):
        characters.extend(list('1234567890')) 
  
  thepassword = ''
  
  length = int(request.GET.get('length',12))

  for item in range(length):
        thepassword += random.choice(characters)
      
  
  return render(request, 'generator/password.html', {'password' : thepassword})