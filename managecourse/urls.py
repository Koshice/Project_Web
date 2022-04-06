from django.urls import path
from . import views


urlpatterns = [
    path("category/", views.category_view),
    path("category/<int:id>", views.category_details),
    path("category/add", views.category_add),
    path("category/delete/<int:id>", views.category_delete),
    path("category/update/<int:id>", views.category_update),
    path("example_01", views.show_example_01),
    path("example_02", views.show_example_02),
]
