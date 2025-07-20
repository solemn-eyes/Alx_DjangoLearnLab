from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_id):
    return Book.objects.filter(author_id=author_id)

# List all books in a library
def get_books_in_library(library_id):
    return Book.objects.filter(library_id=library_id)

# Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    try:
        library = Library.objects.get(id=library_id)
        return library.librarian  # Assuming a OneToOneField or ForeignKey to Librarian
    except Library.DoesNotExist:
        return None
    
