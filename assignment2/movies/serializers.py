from rest_framework import serializers
from .models import Movies


class MoviesSerializers(serializers.ModelSerializer):
    '''Serializer for Movies Model'''
    class Meta:
        model = Movies
        fields = "__all__"