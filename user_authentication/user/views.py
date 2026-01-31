from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

def register_view(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Register Successfull")
            return redirect("user_dashboard")
        else:
            messages.error(request,"Registration failed")
    else:
        form=RegistrationForm()
    return render(request,"register.html",{"form":form})

def login_view(request):
    pass