from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=255)
    dept = models.CharField(max_length=100)
    sal = models.FloatField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    eligible = models.BooleanField()
