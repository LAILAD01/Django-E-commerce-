from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['brand','model_name', 'image','model_no', 'os', 'processor_type', 'processor_gen', 'ram', 'disc_size', 'disc_type', 'screen_size', 'rating', 'price', 'site_name']
    search_fields = ['brand','model_name', 'model_no', 'os', 'processor_type', 'processor_gen', 'ram', 'disc_size', 'disc_type', 'screen_size', 'rating', 'price', 'site_name']

admin.site.register(Product, ProductAdmin)
