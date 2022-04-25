import code
from unicodedata import name
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField()
    name_en = models.CharField(max_length=250)
    name_vi = models.CharField(max_length=250)
    credit = models.IntegerField()
    hour = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " (" + self.name_en + ")"


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
