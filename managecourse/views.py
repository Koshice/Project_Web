from django.shortcuts import redirect, render
from .models import Category
from django.http import HttpResponse

# Create your views here.

# CRUD
# Read
# View All Categories
def category_view(request):
    category = Category.objects.all()
    return HttpResponse(category)


# Read
# View Details of 01 Category
def category_details(request, id):
    category = Category.objects.get(id=id)
    return HttpResponse(category)


# Create
def category_add(request):
    category = Category(
        name="Category 05",
        description="Category 05",
    )

    category.save()

    return redirect(category_view)


# Delete
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()

    return redirect(category_view)


# Update
def category_update(request, id):
    category = Category.objects.get(id=id)
    category.name = "Category New"

    category.save()

    return redirect(category_view)
