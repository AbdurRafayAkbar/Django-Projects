from django.shortcuts import render,redirect

def login_view(request):
    if request.method=="POST":
        name=request.POST.get("name")

        request.session['username']=name
        request.session["visit"]=0  

        return redirect("home")
    return render(request,"login.html")

def home(request):
    if "username" not in request.session:
        return redirect("login")
    
    request.session['visit']+=1

    context={
        'name':request.session["username"],
        "visit":request.session['visit']
    }
    return render(request,"home.html",context)

def logout_view(request):
    request.session.flush()
    return redirect("login_view")
