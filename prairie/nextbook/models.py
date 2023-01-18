from django.db import models

from django.db.models import Max
import random

# Create your models here.

class RandomManager(models.Manager):

    def get_query_set(self):
        return super(RandomManager, self).get_query_set().order_by('?')



class Book(models.Model):

    def lib_total():
        return Book.objects.count() + 1

    book_number = models.IntegerField(default=lib_total, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    objects = models.Manager()
    randoms = RandomManager()

    def __str__(self):
        return self.title

    def get_random():
        max_id = Book.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            randbook = Book.objects.filter(pk=pk).first()
            if randbook:
                return randbook