from django.contrib import admin

from .models import Country, City

admin.site.register(City)
admin.site.register(Country)
