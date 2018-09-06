from django.contrib import admin

from .models import Category, Product, ProductVariant

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant)
