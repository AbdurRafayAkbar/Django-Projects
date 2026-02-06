from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("dark/",views.dark_mode,name="dark_mode"),
    path("light/",views.light_mode,name="light_mode")
]
