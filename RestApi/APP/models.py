from django.db import models
from rest_framework.authtoken.models import Token



# Create your models here.







class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) :
        return self.category_name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)

    def __str__(self):
        return self.book_title



class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    