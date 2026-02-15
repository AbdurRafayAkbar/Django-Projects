from django.shortcuts import render,redirect,get_object_or_404
from .models import expense_model
from .forms import expense_forms
from django.contrib import messages

def add_expense(request):
    form = expense_forms()
    if request.method == "POST":
        form = expense_forms(request.POST)
        if form.is_valid():
            form.save()
            print("Saved Successfully")
            return redirect("all_expenses")
        else:
            print(form.errors)   # ADD THIS
    return render(request, "add_expense.html", {
        "form": form
    })

def all_expenses(request):
    expenses = expense_model.objects.all()
    return render(request,"all_expenses.html",{
        "expenses":expenses
    })

def delete_expense(request,pk):
    expense=expense_model.objects.get(pk=pk)
    expense.delete()
    return redirect("all_expenses")

def update_expense(request,pk):
    expense=get_object_or_404(expense_model,pk=pk)
    if request.method=="POST":
        form=expense_forms(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect("all_expenses")
        else:
            messages.error(request,"Not Valid Info")
    form=expense_forms(instance=expense)
    return render(request,"update_expense.html",{
        "form":form
    })

def describe_expense(request,pk):
    expense=expense_model.objects.get(pk=pk)
    return render(request,'describe_expense.html',{
        "expense":expense
    })