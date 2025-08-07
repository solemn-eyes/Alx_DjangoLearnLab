from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializer for the Author model   
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    books = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
    