from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Electronics

@admin.register(Electronics)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price')  
    search_fields = ('name', 'brand')          
    list_filter = ('brand',) 