from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    book_list = [f"{book.title} by {book.author}" for book in books]
    return render(request, 'books_list.html', {'book_list': book_list})

    class LibraryDetailView(DetailView):
        model = Library
        template_name = 'library_detail.html'
        context_object_name = 'library'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['books'] = self.object.book_set.all()
            return context

