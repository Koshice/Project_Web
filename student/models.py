import imp
from django.db import models
from course.models import Course

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    staff_id = models.CharField(max_length=5)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name + " (" + self.email + ")"
