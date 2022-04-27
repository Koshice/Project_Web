from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.student_index),
    path("student/<int:id>", views.student_details),
    path("student/add", views.student_add),
    path("student/delete/<int:id>", views.student_delete),
    path("student/edit/<int:id>", views.student_edit),
    path("student/back_to_studentlist", views.back_to_studentlist),
    path("student/edit/back_to_studentlist", views.back_to_studentlist),
]
