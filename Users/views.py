# from .models import User
import email
from . import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def auth(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email  = request.POST['email']
        password = request.POST['password']
        obj = models.User()
        obj.name = name
        obj.phone = phone
        obj.email = email
        obj.password = password
        obj.save()
        return redirect('../')
    else:
        return HttpResponseRedirect("../signup")
def signup(request):
    return render(request,'user.html',{"mmd":AuthenticationForm})
    