from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_books_with_the = Book.objects.filter(title__icontains='the').count()
    num_genres_with_fiction = Genre.objects.filter(name__icontains='fiction').count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_with_the': num_books_with_the,
        'num_genres_with_fiction': num_genres_with_fiction,
    }

    return render(request, 'index.html', context=context)
