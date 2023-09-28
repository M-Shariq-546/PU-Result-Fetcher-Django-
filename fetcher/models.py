from django.db import models
# student_info/models.py
class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=20)
    # Define any other fields needed




# Create your models here.
