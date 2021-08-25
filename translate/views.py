from django.shortcuts import render, redirect, resolve_url
from .models import Author
from .forms import AuthorForm
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect


def create(request):

    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        print('1')
        if form.is_valid():
            print('3')
            author = form.save(commit=False)
            author.create_date = timezone.now()
            author.save()
            print('3')

            return redirect('translate:create')
        else:
            print('5')

    else:
        form = AuthorForm()
        print('4')
    print('2')
    return render(request, 'landing_page.html', {'form': form})

