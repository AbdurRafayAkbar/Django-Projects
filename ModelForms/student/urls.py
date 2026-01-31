from django.urls import path
from . import views

urlpatterns = [
    path("add/",views.student_create,name="student_create"),
    path("read/",views.all_students,name="all_students"),
    path("each_student/<int:pk>/",views.each_student,name="each_student"),
    path("edit_student/<int:pk>/",views.edit_student,name="edit_student"),
    path("delete_student/<int:pk>",views.delete_student,name="delete_student")
]
