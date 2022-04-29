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

    path("result/", views.result_index),
    path("result/<int:id>", views.result_details),
    path("result/add", views.result_add),
    path("result/delete/<int:id>", views.result_delete),
    path("result/edit/<int:id>", views.result_edit),
    path("result/back_to_resultlist", views.back_to_resultlist),
    path("result/edit/back_to_resultlist", views.back_to_resultlist),
]
