from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.urls import reverse

class BookAPITests(APITestCase):
    def setUp(self):
        # Creating a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Creating an Auth token for the user
        self.client.login(username='testuser', password='testpassword')

         # Create a book in the DB for testing retrieve/update/delete
        self.book = Book.objects.create(title="Test Book", author="Test Author", description="Test Description")
        
        # Define URLs
        self.list_url = reverse("book-list")  # GET all books
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

    # ------------------ LIST ------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    # ------------------ RETRIEVE ------------------
    def test_retrieve_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    # ------------------ CREATE ------------------
    def test_create_book_authenticated(self):
        data = {"title": "New Book", "author": "New Author", "description": "New Description"}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        data = {"title": "Fail Book", "author": "No Auth", "description": "Should Fail"}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------ UPDATE ------------------
    def test_update_book_authenticated(self):
        data = {"title": "Updated Title", "author": "Updated Author", "description": "Updated"}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_update_book_unauthenticated(self):
        self.client.logout()
        data = {"title": "Should Fail", "author": "No Auth", "description": "Fail"}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------ DELETE ------------------
    def test_delete_book_authenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_delete_book_unauthenticated(self):
        self.client.logout()
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        