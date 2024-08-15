from django.db import models

class login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    usertype = models.CharField(max_length=150)
    
class Register(models.Model):
    Name = models.CharField(max_length=300)
    Phone_number = models.CharField(max_length=300)
    mail = models.EmailField(max_length=300)
    Password = models.CharField(max_length=300)
    confirm_password = models.CharField(max_length=300)