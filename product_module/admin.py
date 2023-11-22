from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_filter = ['category', 'is_active']
    list_editable = ['price', 'is_active']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
