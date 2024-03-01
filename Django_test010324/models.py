from django.contrib.auth.models import User
from django.db import models


class ProductManager(models.Manager):
    pass


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    allowed_users = models.ManyToManyField(User, related_name='accessible_products')
    objects = ProductManager()


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    objects = ProductManager()


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    users = models.ManyToManyField(User, related_name='groups')
