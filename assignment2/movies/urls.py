from django.urls import path
from .views import homepage, rating

app_name='movies'

urlpatterns = [
    path('', homepage, name='home'),
    path('rate/', rating, name='rate'),
]
