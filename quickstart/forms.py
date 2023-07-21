from django import forms
from django.conf import settings
import requests


class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        print('api_key', word)
        endpoint = 'https://dictionaryapi.com/api/v3/references/sd2/json/{word}/?key={api_key}'
        url = endpoint.format(word=word, api_key=settings.DICTIONARY_KEY)
        print(url)
        response = requests.get(url)
        print('response', response)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
        else:
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The Merriam Webster dicitonary API is not available at the moment or we have hit the daily limit. Please try again later.'
        return result
