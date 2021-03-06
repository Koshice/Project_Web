from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("course.urls")),
    path("course/", include("course.urls")),
    path("student/", include("student.urls")),
]
