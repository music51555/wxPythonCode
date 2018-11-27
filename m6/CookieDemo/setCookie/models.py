from django.db import models

class UserClass(models.Model):
    nid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)