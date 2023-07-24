from django.shortcuts import render
from requests import Response, request
import requests
from rest_framework import viewsets
import urllib.parse
from currency import settings
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.views import APIView
from rest_framework import status


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoDefineView(APIView):
    serializer_class = TodoSerializer

    # def get(self, request, *args, **kwargs):
    #     id = request.GET['id']
    #     obj = InventoryLedger.objects.filter(product__product__short_code=id)
    #     serializer = InventoryLedgerListSerializer(obj, many=True)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, id):
        # id = request.GET['id']
        obj = Todo.objects.filter(id=id).first()
        print('id--------------------------->', obj)

        endpoint = 'https://dictionaryapi.com/api/v3/references/sd2/json/{word}/?key={api_key}'
        url = endpoint.format(word=urllib.parse.quote_plus(
            obj.title), api_key=settings.DICTIONARY_KEY)
        response = requests.get(url)
        # {% for definition in search_result.shortdef % }
        #     <li > {{definition}} < /li >
        # {% endfor % }

        # print('response------------------------------>', response.json())

        response_data = response.json()
        print('response----->', response_data[0]['shortdef'])
        if response.status_code == 200:  # SUCCESS
            result = response_data[0]['shortdef']
        else:
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % obj.title
            else:
                result['message'] = 'The Merriam Webster dicitonary API is not available at the moment or we have hit the daily limit. Please try again later.'
        return result

        # return Response(obj.title)
        # get_queryset = Todo.objects.filter(id=pk)
        # return queryset
    #     return 'hi'
    #     result = {}
    #     word = self.cleaned_data['word']
