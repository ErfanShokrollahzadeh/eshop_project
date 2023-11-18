from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields =['slug']
    prepopulated_fields = {'slug': ['title',]} # auto generate slug field
    list_display = ['__str__','price','rating','is_active'] # show fields in admin panel
    list_filter = ['is_active','rating'] # show filter in admin panel
    list_editable = ['price','rating'] # edit fields in admin panel


admin.site.register(models.Product, ProductAdmin)
