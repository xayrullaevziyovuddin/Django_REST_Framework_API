from rest_framework import viewsets
from .serializers import AuthorModelSerializer, BookModelSerializer
from .models import Author, Book


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelSerializer(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
