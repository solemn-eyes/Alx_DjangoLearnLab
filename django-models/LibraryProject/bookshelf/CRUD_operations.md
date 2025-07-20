### CREATE
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

### RETRIEVE
book = Book.objects.get(title="1984")
book.title
book.author
book.publication_year

### UPDATE
book.title ="Nineteen Eighty-four"
book.save()
book.title

### DELETE
book.delete()
Book.objects.all()