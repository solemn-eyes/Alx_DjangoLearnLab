from django.db import models
from rest_framework import DjangoFilterBackend, filters

# Create your models here.

# Creating the Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

# Creating the Book model
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey.one_to_many('Author', on_delete=models.CASCADE, related_name='books')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']


