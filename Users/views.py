from . import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


# Create your views here.
def auth(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,
                                 email='',
                                 password=password)
        return redirect('../login')
    else:
        return redirect("../signup")
def signup(request):
    return render(request,'user.html',{})
def login(request):
    return render(request,'login.html',{})
