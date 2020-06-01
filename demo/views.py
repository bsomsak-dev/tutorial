from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book


class Another(View):
    book = Book.objects.get(id=1)
    output = f"We have {book.title} books in DB with book ID {book.id}<br>"

    # for book in books:
    #     output += f"We have {book.title} books in DB with book ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse("First message from views")
