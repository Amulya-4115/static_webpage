from django.db import models

# Create your models here.
class student(models.Model):
    id_num=models.IntegerField(max_length=10)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

# Create your models here.
