from django.db import models

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    pub_date=models.DateField()
    publish=models.CharField(max_length=20)

    def __str__(self):
        return self.title