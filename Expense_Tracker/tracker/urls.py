from django.urls import path
from . import views

urlpatterns = [
    path("add_expense/",views.add_expense,name="add_expense"),
    path("all_expenses/",views.all_expenses,name="all_expenses"),
    path("delete_expense/<int:pk>/",views.delete_expense,name="delete_expense"),
    path("update_expense/<int:pk>/",views.update_expense,name="update_expense"),
    path("describe_expense/<int:pk>/",views.describe_expense,name="describe_expense")
]
