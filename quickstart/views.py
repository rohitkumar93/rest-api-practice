from django.shortcuts import render
from django.conf import settings
import requests
from .forms import DictionaryForm


def dictionary(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
        search_result[0] = {}
    if (len(search_result)):
        return render(request, 'dictionary.html', {'form': form, 'search_result': search_result[0]})
