from django.db import models
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.book.title} ({self.id})'
