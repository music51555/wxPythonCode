from django.db import models

class User(models.Model):
    nid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=5)
    password=models.CharField(max_length=20,default=0)
    r_password=models.CharField(max_length=20)
    email=models.EmailField()
    tel=models.CharField(max_length=11)