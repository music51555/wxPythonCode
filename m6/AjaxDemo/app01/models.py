from django.db import models

class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)

class Book(models.Model):
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=5,decimal_places=2)
