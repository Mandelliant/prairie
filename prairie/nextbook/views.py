from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random

def suggestion(request):

    books = Book.get_random()

    return render(request, 'nextbook/index.html', {'books': books})
