from . import views
from django.urls import path

urlpatterns = [
    path("register/",views.register_view,name="register"),
    path("login/",views.login_view,name="user_login"),
    path("logout/",views.logout_view,name="user_logout"),
    path("dashboard/",views.dashboard,name="user_dashboard"),
]
