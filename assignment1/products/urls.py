from django.urls import path
from .views import ProductsAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView

app_name = 'products'

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name="products"), #API for CRUD operations on Product model
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair') #API to create the refresh and access token
]
