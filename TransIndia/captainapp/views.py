from django.shortcuts import render, redirect
from pyexpat.errors import messages
from captainapp.models import CaptainModel
from django.contrib import messages
from atexit import register
from sre_constants import SUCCESS
from captainapp import *
import re
from tabnanny import check
from unicodedata import name
# Create your views here.

def captain_register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        city=request.POST.get('city')
        vehicle=request.POST.get('vehicle')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('cpwd')

        if CaptainModel.objects.filter(cap_mobile=mobile):
            messages.error(request,'mobile already exists')
        elif CaptainModel.objects.filter(cap_email=email).exists():
            messages.error (request, "Email already exist")
        else:
            captain_register = CaptainModel.objects.create(cap_name=name,cap_email=email,cap_mobile=mobile,city=city,cap_vehicle=vehicle,pwd=pwd,con_pwd=cpwd)
            captain_register.save()
            messages.success(request, "Account created successful")
            return redirect('cap_login')
        
    return render(request,'main/captain-register.html')

def captain_login(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        pwd = request.POST.get('pwd')
        try:
            check = CaptainModel.objects.get(cap_mobile=mobile,pwd=pwd)
            request.session['cap_id']=check.cap_id
            return redirect('cap_home')
            messages.error(request,'invalied login')
        except:
            pass
    return render(request,'main/captain-login.html')

def captain_home(request):
    return render(request,'main/captain-home.html')

def captain_profile(request):
    cap_id = request.session["cap_id"]
    data = CaptainModel.objects.get(cap_id=cap_id)
    return render(request,'main/captain-profile.html',context={'data':data})

def captain_payment(request):
    return render(request,'main/captain-payment.html')

def captain_order(request):
    return render(request,'main/captain-order.html')

def captain_feedback(request):
    return render(request,'main/captain-feedback.html')