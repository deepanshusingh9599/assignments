from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    '''Serializer for Product Model'''
    class Meta:
        model = Product
        fields = "__all__"
