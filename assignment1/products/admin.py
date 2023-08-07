from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin Model class for Product Model. '''

    list_display = ['id', 'name', 'description', 'quantity', 'price']
