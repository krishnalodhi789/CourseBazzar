from typing import Any
from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime


class CustomUser(AbstractUser):
    is_buyer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)
    gender =  models.CharField(max_length=32,choices=(('male',"Male"),("female", "Female"),("other", "Other")))
    image = models.ImageField(upload_to='Profile/', default='Profile/pic.png')

class CourseCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    
class Course(models.Model):
    user =  models.ForeignKey(CustomUser, related_name='courses', on_delete=models.CASCADE)
    category = models.OneToOneField(CourseCategory, related_name='category', on_delete=models.CASCADE)
    title =  models.CharField(max_length=50)
    key_points = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(max_length=5000)
    price = models.IntegerField()
    sale_counter = models.IntegerField(default=0)
    published_datetime = models.DateTimeField(default=datetime.datetime.now())
    approval_datetime = models.DateTimeField(blank=True, null=True)
    approve = models.BooleanField(default = False)
    image = models.ImageField(upload_to="Course Image/")
    course_file = models.FileField( upload_to='Courses/')
    
    def __str__(self):
        return self.title
    
    
class AddToCart(models.Model):
    user =  models.ForeignKey(CustomUser, related_name='carts', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='carts', on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)

class Wallet(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='wallet')
    balance = models.FloatField(default=0)
    
class AmountTransitionHistory(models.Model):
    user = models.ForeignKey(CustomUser, related_name='amounttransitionhistory', on_delete=models.CASCADE)
    status =  models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    datetime = models.DateTimeField(default=datetime.datetime.now())


class CourseHistory(models.Model):
    buyer = models.ForeignKey(CustomUser,related_name='buyhistories', on_delete=models.CASCADE)
    course = models.ForeignKey(Course,related_name='coursebuyhistories', on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.datetime.now()) 
    seller = models.ForeignKey(CustomUser,related_name='salehistories', on_delete=models.CASCADE)


class CourseOffer(models.Model):
    saller = models.ForeignKey(CustomUser,related_name='courseoffer', on_delete=models.CASCADE)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    offer = models.IntegerField(default=0) 
    remaining_amount = models.FloatField(default=0.0)