from django.urls import path
from .views import MyAPIView

urlpatterns = [
    path('books', 'book/create/', name='book_create'),
    path('books/<int:book_id>/', 'book/detail/', name='book_detail'),
    path('books/<int:book_id>/update/', 'book/update/', name='book_update'),
    path('books/<int:book_id>/delete/', 'book/delete/', name='book_delete'),
    path('my-api/', MyAPIView.as_view(), name='my_api'),  
]
