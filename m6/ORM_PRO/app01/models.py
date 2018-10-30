from django.db import models

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)
    pub_date=models.DateField()
    state=models.BooleanField()
    public=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=8,decimal_places=2)