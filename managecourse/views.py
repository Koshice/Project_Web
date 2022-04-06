import os
from django.shortcuts import redirect, render
from .models import Category, Course
from django.http import HttpResponse

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

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


# Call example_01.html
def show_example_01(request):
    return render(request, "courses/example_01.html")


# Call example_02.html
def show_example_02(request):
    num_1 = 1
    category = Category.objects.all()

    context = {
        "num_01": num_1,
        "abc": "This is abc.",
        "category": category,
    }

    return render(request, "courses/example_02.html", context)
