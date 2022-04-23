from pyexpat.errors import messages
from django.shortcuts import render, redirect
from userapp.models import *
from userapp.models import UserModel
from django.contrib import messages
from atexit import register
from sre_constants import SUCCESS
from userapp import *
import re
from tabnanny import check
from unicodedata import name
# Create your views here.

def user_booking(request):
    return render(request,'main/user-booking.html')

def user_home(request): 
    return render(request,'main/user-home.html')

def user_profile(request):
    user_id = request.session["user_id"]
    data = UserModel.objects.get(user_id=user_id)
    return render(request,'main/user-profile.html',{'data':data})

def user_register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('cpwd')
        
        # server validation for user_register

        # if len(name) > 10:
        #     messages.error (request, "user name must be 10 characters")
        # elif not name.isalpha():
        #     print("username should only contain letters")
        #     messages.error (request, "username should only contain letters")
        # elif len(pwd) < 8:
        #     messages.error (request, "Make sure your password is atleast 8 letters")
        # elif re.search('[0-9]', pwd) is None:
        #     messages.error (request, "Make sure your password has a number in it")
        # elif re.search('[A-Z]',pwd) is None:
        #     messages.error (request, "Make sure your password has a capital letter in it")

        if UserModel.objects.filter(user_mobile=mobile):
            messages.error(request,'mobile already exists')
        elif UserModel.objects.filter(user_email=email).exists():
            messages.error (request, "Email already exist")
        else:
            user_register = UserModel.objects.create(user_name=name,user_email=email,user_mobile=mobile,pwd=pwd,con_pwd=cpwd)
            user_register.save()
            messages.success(request, "Account created successful")
            return redirect('user_login')
            
    return render(request,'main/user-register.html')

def user_login(request):
    # server validation for user_login
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        pwd = request.POST.get('pwd')
        try:
            check = UserModel.objects.get(user_mobile=mobile,pwd=pwd)
            request.session['user_id']=check.user_id
            return redirect('user_home')
            messages.error(request,'invalied login')
        except:
            pass
    return render(request,'main/user-login.html')