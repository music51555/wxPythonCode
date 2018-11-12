from django.db import models

class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    pubdate=models.DateField()
    publish=models.ForeignKey(to='Publish',to_field='nid',on_delete=models.CASCADE)
    authors=models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title

class Publish(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Author(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.name




