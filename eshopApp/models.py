from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    role=models.CharField(max_length=50)
    password = models.CharField(max_length=255)

class Products(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    product_image = models.ImageField(upload_to='products/')
    price = models.FloatField()

    def __str__(self):
        return self.product_name

class Services(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.service_name

class Categories(models.Model):
    category_id = models.CharField(unique=True, max_length=20)
    category_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    role=models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username