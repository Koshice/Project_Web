import code
from unicodedata import name
from django.db import models

from course.models import ClassRoom, Course

# Create your models here.
# Model Student


class Student(models.Model):
    student_code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    email = models.EmailField(max_length=30)
    dob = models.CharField(max_length=11)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (" + self.student_code + ")"

        # Model Result


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.student + self.mark
