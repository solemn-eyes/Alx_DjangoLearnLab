from django.urls import path
from . import views

urlpatterns = [
    # Function-based views
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),

    # Class-based views
    path('books-cbv/', views.BookListView.as_view(), name='book_list_cbv'),
    path('authors-cbv/', views.AuthorListView.as_view(), name='author_list_cbv'),
]