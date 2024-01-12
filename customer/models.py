from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, related_name='customer')
    phone = models.CharField(max_length=15)
    gender =  models.CharField(max_length=32,choices=(('male',"Male"),("female", "Female"),("other", "Other")))
    image = models.ImageField(upload_to='Profile/', default='Profile/pic.png')

    def __str__(self):
        return self.user.username
    
class Course(models.Model):
    customer =  models.ForeignKey(Customer, related_name='courses', on_delete=models.CASCADE)
    title =  models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    price = models.IntegerField()
    sale_counter = models.IntegerField(default=0)
    published_datetime = models.DateTimeField(auto_now=True)
    approval_datetime = models.DateTimeField(blank=True, null=True)
    approve = models.BooleanField(default = False)
    image = models.ImageField(upload_to="Course Image/")
    course_file = models.FileField( upload_to='Courses/')
    
    
class AddToCart(models.Model):
    customer =  models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)

class Wallet(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='wallet')
    balance = models.FloatField(default=0)
    
class AmountTransitionHistory(models.Model):
    user = models.ForeignKey(User, related_name='amounttransitionhistory', on_delete=models.CASCADE)
    status =  models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    datetime = models.DateTimeField(auto_now=True)
    
    