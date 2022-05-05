from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.category_index),
    path("category/<int:id>", views.category_details),
    path("category/add", views.category_add),
    path("category/delete/<int:id>", views.category_delete),
    path("category/edit/<int:id>", views.category_edit),
    path("category/back_to_categorylist", views.back_to_categorylist),
    path("category/edit/back_to_categorylist", views.back_to_categorylist),

    path("course/", views.course_index),
    path("course/<int:id>", views.course_details),
    path("course/add", views.course_add),
    path("course/delete/<int:id>", views.course_delete),
    path("course/edit/<int:id>", views.course_edit),
    path("course/back_to_courselist", views.back_to_courselist),
    path("course/edit/back_to_courselist", views.back_to_courselist),

    path("classroom/", views.classroom_index),
    path("classroom/<int:id>", views.classroom_details),
    path("classroom/add", views.classroom_add),
    path("classroom/delete/<int:id>", views.classroom_delete),
    path("classroom/edit/<int:id>", views.classroom_edit),
    path("classroom/back_to_classroomlist", views.back_to_classroomlist),
    path("classroom/edit/back_to_classroomlist", views.back_to_classroomlist),

    path("course/login", views.admin_login),
    path("course/logout", views.admin_login),

    path("home/", views.show_home),


]
