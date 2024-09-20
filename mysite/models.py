from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=100)
    processor_gen = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    disc_size = models.CharField(max_length=100)
    disc_type = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MaxValueValidator(5)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    site_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.brand
    
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s Cart - {self.product.name}"
    
class User(AbstractUser):
    #username = models.CharField(max_length=150)
    #birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email