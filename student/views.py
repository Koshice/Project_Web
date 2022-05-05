from operator import index
from django.shortcuts import render, redirect

from course.models import ClassRoom, Course
from .models import Student, Result
from .forms import StudentForm, ResultForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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


@login_required(login_url="../login")
def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(student_index)


@login_required(login_url="../student/login")
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


@login_required(login_url="../login")
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

    # CRUD Result.


def result_index(request):
    results = Result.objects.all()
    context = {
        "results": results,
    }
    return render(request, "student/result/result_index.html", context)


@login_required(login_url="../../student/login")
def result_delete(request, id):
    result = Result.objects.get(id=id)
    result.delete()
    return redirect(result_index)


@login_required(login_url="../student/login")
def result_add(request):
    form = ResultForm(request.POST or None)

    if form.is_valid():
        result = Result()

        result.mark = request.POST["mark"]

        student = Student.objects.get(id=int(request.POST["student"]))
        result.student = student

        course = Course.objects.get(id=int(request.POST["course"]))
        result.course = course

        classroom = ClassRoom.objects.get(id=int(request.POST["classroom"]))
        result.classroom = classroom

        result.save()

        return redirect(result_index)

    context = {"form": form}

    return render(request, "student/result/result_add.html", context)


@login_required(login_url="../../student/login")
def result_edit(request, id):
    result = Result.objects.get(id=id)
    form = ResultForm(request.POST or None, instance=result)

    if form.is_valid():

        result.mark = request.POST['mark']

        student = Student.objects.get(id=int(request.POST["student"]))
        result.student = student

        course = Course.objects.get(id=int(request.POST["course"]))
        result.course = course

        classroom = ClassRoom.objects.get(id=int(request.POST["classroom"]))
        result.classroom = classroom

        form.save()

        return redirect(result_index)

    context = {"form": form}

    return render(request, "student/result/result_edit.html", context)


def total_count(request):
    courses_count = Course.objects.all().count()
    classes_count = ClassRoom.objects.all().count()
    student_count = Student.objects.all().count()
    mark_count = Result.objects.all().count()
    context = {
        'courses_count': courses_count,
        'classes_count': classes_count,
        'student_count': student_count,
        'mark_count': mark_count,
    }
    return render(request, 'course/home.html', context)


def back_to_resultlist(request):
    return redirect(result_index)


def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        admin = authenticate(username=username, password=password)

        if admin is not None and admin.is_active:
            login(request, admin)
            return redirect(student_index)

    return render(request, "student/login.html")


def admin_logout(request):
    logout(request)
    return redirect(student_index)
