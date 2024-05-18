import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'published_date']
    search_fields = ['title', 'author']
    ordering = ['published_date']


def export_books_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    # Write the headers
    writer.writerow(['ID', 'Title', 'Author', 'Published Date', 'ISBN'])

    # Write the data
    books = Book.objects.all()
    for book in books:
        writer.writerow([book.id, book.title, book.author, book.published_date, book.isbn])

    return response


# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'published_date', 'isbn']
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'published_date', 'isbn']
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
