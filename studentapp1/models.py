from django.db import models

class Student(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    m1 = models.CharField(max_length=100)
    m2 = models.CharField(max_length=100)
    m3 = models.CharField(max_length=100)
# Create your models here.
