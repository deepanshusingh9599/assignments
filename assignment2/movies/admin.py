from django.contrib import admin
from .models import Movies


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    '''Admin Model for Movies'''
    list_display = ['id','name','rating','year']
