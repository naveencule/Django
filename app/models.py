from django.db import models

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Login(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
