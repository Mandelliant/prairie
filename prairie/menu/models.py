from django.db import models
import random

class Book(models.Model):
    book_number = models.IntegerField(default=1, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def random(self):
        random_book = random.choice
        return random_book