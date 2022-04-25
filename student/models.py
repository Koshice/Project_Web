import code
from unicodedata import name
from django.db import models

from course.models import Course

# Create your models here.

class Student(models.Model):
    student_code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    email = models.EmailField(max_length=30)
    dob = models.CharField(max_length=11)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (" + self.email + ")"
