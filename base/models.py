from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    nic = models.CharField(max_length=12)
    address = models.TextField()
    school = models.CharField(max_length=100)
    email = models.EmailField()
