from rest_framework import serializers
from .models import Author, Book


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
