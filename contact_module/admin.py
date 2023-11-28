from django.contrib import admin
from . import models

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title','created_date']

admin.site.register(models.ContactUs, ContactUsAdmin)