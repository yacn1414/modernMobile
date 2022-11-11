from . import models
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login

# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return redirect('/account')
            else:
                messages.ERROR(request,'مشکلی در ثبت نام وجود دارد')
                return redirect('/login')
    return redirect('/login')
    # half login
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
def loginUser(request):
    return render(request,'registration/login.html',{})
