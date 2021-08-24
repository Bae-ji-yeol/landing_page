from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Data
from .forms import AuthorForm
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    author = get_object_or_404(Author)
    return render (request,'landing_page.html' , {'author':author})


def create(request, author_id ):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            author = form.save(commit=False)

            return HttpResponseRedirect('')

    else:
        form = AuthorForm()

    context = {'form': form, 'author':author}
    return redirect('translate:index')
