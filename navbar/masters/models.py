from django.db import models


class City(models.Model):
    name = models.CharField(max_length=127)


class Country(models.Model):
    name = models.CharField(max_length=127)
