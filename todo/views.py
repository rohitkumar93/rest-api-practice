from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo import serializers, models


class TodoList(APIView):
    def get(self, request, format=None):
        todo_lists = models.TodoList.objects.all()
        serializer = serializers.TodoList(todo_lists, many=True)

    def post(self, request, format=None):
        serializer = serializers.TodoList(data=request.data)
        if (serializers.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
