from django.db import models


class Product(models.Model):
    sku = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
