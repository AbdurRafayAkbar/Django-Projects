from django.shortcuts import render,redirect
from .models import Images
from .forms import ImageUploadForm
from django.contrib import messages

def upload_image(request):
    if request.method=="POST":
        form=ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Image uploaded Successfully")
            return redirect("gallery")
        else:
            messages.error(request,"Failed To upload Image")
    else:
        form=ImageUploadForm()
    return render(request,"upload_image.html",{"form":form})

def gallery(request):
    images=Images.objects.all()
    return render(request,"gallery.html",{"images":images})