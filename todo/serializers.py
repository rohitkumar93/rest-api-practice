from rest_framework import serializers
from todo import models

class TodoListItem(serializers.ModelSerializer):
    class Meta:
        model = models.TodoListItem
        fields= ('id','todo_list_id','title','description')
    
    
    
class TodoList(serializers.ModelSerializer):
    items = TodoListItem(many=True)
    
    class Meta:
        model = models.TodoList
        fields = ('id','title','items')
    
    def create(self,validated_data):
        items_data = validated_data.pop('items')
        todo_list = models.TodoList.objects.create(**validated_data)
        for item_data in items_data:
            item_data['todo_list_id'] = todo_list.id
            models.TodoListItem.objects.create(**item_data)
        return todo_list