from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from menu.models import Book
from .forms import AddBook
from nextbook.models import Book
from django.contrib import messages





def library(request):
    form = AddBook(request.POST or None)
    complete_form = form
    success = False
    if request.method == 'POST':
        if form.is_valid():
            addedbook = form.save(commit=False)
            addedbook.save()
            form = AddBook()
            success = True
            nbt = complete_form.cleaned_data['title']
            nba = complete_form.cleaned_data['author']
            messages.success(request, "{} by {} added to your library".format(nbt, nba))


            #messages.success(request, "Book added")


    return render(request, 'newbook/index.html', {'form': form})