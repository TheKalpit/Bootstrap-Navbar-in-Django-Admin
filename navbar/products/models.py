from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=127)


class Product(models.Model):
    name = models.CharField(max_length=127)


class ProductVariant(models.Model):
    name = models.CharField(max_length=127)
