import re
from django.shortcuts import render, redirect

from course.models import ClassRoom, Course
from .models import Student
from .forms import StudentForm

# CRUD Student.

def student_index(request):
    students = Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, "student/student/student_index.html", context)


def student_details(request, id):
    student = Student.objects.get(id=id)
    context = {
        "student": student,
    }
    return render(request, "student/student/student_details.html", context)


def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(student_index)


def student_add(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        student = Student()

        student.student_code = request.POST["student_code"]
        student.name = request.POST["name"]
        student.address = request.POST["address"]
        student.email = request.POST["email"]
        student.dob = request.POST["dob"]

        course = Course.objects.get(id=int(request.POST["course"]))
        student.course = course

        classroom = ClassRoom.objects.get(id=int(request.POST["classroom"]))
        student.classroom = classroom

        student.save()

        return redirect(student_index)

    context = {"form": form}

    return render(request, "student/student/student_add.html", context)


def student_edit(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        
        student.student_code = request.POST["student_code"]
        student.name = request.POST["name"]
        student.address = request.POST["address"]
        student.email = request.POST["email"]
        student.dob = request.POST["dob"]

        course = Course.objects.get(id=int(request.POST["course"]))
        student.course = course

        classroom = ClassRoom.objects.get(id=int(request.POST["classroom"]))
        student.classroom = classroom

        form.save()

        return redirect(student_index)

    context = {"form": form}

    return render(request, "student/student/student_add.html", context)


def back_to_studentlist(request):
    return redirect(student_index)
