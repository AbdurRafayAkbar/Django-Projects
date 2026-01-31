from django.shortcuts import render,get_object_or_404,redirect
from .forms import StudentForm
from .models import Student

def student_create(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"Success.html")
    return render(request,"add_student.html",{"form":form})

def all_students(request):
    all_students=Student.objects.all()
    return render(request,"students_data.html",{"all_students":all_students})

def each_student(request,pk):
    single_student=get_object_or_404(Student,pk=pk)
    return render(request,"each_student.html",{"single_student":single_student})

def edit_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("all_students")
    else:
        form=StudentForm(instance=student)
    return render(request,"edit_student.html",{"form":form})

def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect("all_students")
