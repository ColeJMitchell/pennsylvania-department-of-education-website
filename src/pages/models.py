from django.contrib import admin
from django.db import models

class entries(models.Model):
    year = models.IntegerField()
    aun = models.IntegerField()
    county = models.TextField(max_length=1000)
    salary = models.IntegerField()
    name = models.TextField(max_length=1000)

