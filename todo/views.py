from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo import serializers, models


class TodoList(APIView):
    def get(self, request, todo_list_id, format=None):
        print('code is here @ get')
        todo_lists = models.TodoList.objects.all()
        serializer = serializers.TodoList(todo_lists, many=True)
        return Response(serializer.data)

    # def get(self):
    #     return models.TodoList.objects.all()

    def post(self, request, todo_list_id, format=None):
        print('code is here @ post')
        serializer = serializers.TodoList(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_list_id, format=None, *args, **kwargs):
        print('code is here @ delete')
        # try:
        todo_list = models.TodoList.objects.get(id=todo_list_id)
        print('todo_list', todo_list)
        todo_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # except models.TodoList.DoesNotExist:
        # raise Http404


class TodoListItem(APIView):
    def post(self, request, todo_list_id, format=None):
        try:
            todo_list = models.TodoList.objects.get(id=todo_list_id)
            serializer = serializers.TodoListItem(data=request.data)

            if (serializer.is_valid()):
                serializer.validated_data['todo_list_id'] = todo_list_id
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.TodoList.DoesNotExist:
            raise Http404

    def delete(self, request, todo_list_item_id, format=None):
        try:
            item = models.TodoListItem.objects.get(id=todo_list_item_id)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.TodoListItem.DoesNotExist:
            return Http404
