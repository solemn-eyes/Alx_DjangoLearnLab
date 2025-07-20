from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    output = "<h2>All Books</h2><ul>"
    for book in books:
        output += f"<li>{book.title} by {book.author}</li>"
    output += "</ul>"
    return HttpResponse(output)

class BookDetailView(DetailView):
    model = Library
    template_name = 'list_books.html'
    context_object_name = 'book'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    

