from django.shortcuts import render
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin  


# Create your views here.

# Creating views for the Book model

class BookListView(views.View):
    def get(self, request):
        # Logic to retrieve and return a list of books
        return render(request, 'book_list.html')

class BookDetailView(views.View):
    def get(self, request, book_id):
        # Logic to retrieve and return details of a specific book
        return render(request, 'book_detail.html', {'book_id': book_id})
    
class BookCreateView(LoginRequiredMixin, views.View):  # Restrict to authenticated users
    def get(self, request):
        # Logic to display a form for creating a new book
        return render(request, 'book_form.html')

    def post(self, request):
        # Logic to handle the form submission and create a new book
        return render(request, 'book_success.html')
    
class BookUpdateView(LoginRequiredMixin, views.View):  # Restrict to authenticated users
    def get(self, request, book_id):
        # Logic to display a form for updating an existing book
        return render(request, 'book_form.html', {'book_id': book_id})

    def post(self, request, book_id):
        # Logic to handle the form submission and update the book
        return render(request, 'book_success.html', {'book_id': book_id})
    
class BookDeleteView(LoginRequiredMixin, views.View):  # Restrict to authenticated users
    def get(self, request, book_id):
        # Logic to confirm deletion of a book
        return render(request, 'book_confirm_delete.html', {'book_id': book_id})

    def post(self, request, book_id):
        # Logic to handle the deletion of a book
        return render(request, 'book_deleted.html', {'book_id': book_id})