from django.db import models
import datetime


#class Person(models.Model):
   # name = models.CharField(max_length=20)
   # age = models.IntegerField()

class Accountant(models.Model):
    name =models.CharField(max_length=30)

class Employee(models.Model):
    name=models.CharField(max_length=30)
    #time_start=


class Manager(models.Model):
    name=models.CharField(max_length=30)

class Company(models.Model):
    name=models.CharField(max_length=30)


class Storage(models.Model):
    price=models.IntegerField()

class Work(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    time=datetime.time.

class Salary(models.Model):
    price=models.IntegerField()
    time=
    is_time_salary=
    work=Work()
    price=