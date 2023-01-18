from django import forms
from django.db import models
from django.forms import ModelForm
from nextbook.models import Book


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_number', 'title', 'author']