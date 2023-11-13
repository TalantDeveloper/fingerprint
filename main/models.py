from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    icon = models.ImageField(upload_to="./category", default="./category/1234.jpg")


class Customer(models.Model):
    """
    Account Management
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='./user/', default='./user/538642.png')

    def __str__(self):
        return self.user.username


