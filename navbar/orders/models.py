from django.db import models

class Order(models.Model):
    price = models.IntegerField()