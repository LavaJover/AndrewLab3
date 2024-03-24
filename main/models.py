from django.db import models
from django.contrib.auth.models import AbstractUser
class Subject(models.Model):
    name = models.CharField()

class Teacher(models.Model):
    name = models.CharField()
    surname = models.CharField()

class Class(models.Model):
    name = models.CharField()
    lead_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField()
    surname = models.CharField()
    study_class = models.ForeignKey(Class, on_delete=models.CASCADE)

class Journal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    study_class = models.OneToOneField(Class, on_delete=models.CASCADE)
    mark = models.IntegerField()