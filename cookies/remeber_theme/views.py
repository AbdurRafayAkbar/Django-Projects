from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    theme=request.COOKIES.get("theme")
    return render(request,"home.html",{"theme":theme})

def dark_mode(request):
    response=HttpResponse("dark mode activated")
    response.set_cookie("theme","dark",max_age=60*60*7)
    response['Location']="/"
    
    return response
    

def light_mode(request):
    response=HttpResponse("light mode activated")
    response.set_cookie("theme","light",max_age=60*60*7)
    response["Location"]="/"
    return response