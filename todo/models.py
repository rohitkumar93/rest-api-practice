from django.db import models

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=100)


class TodoListItem(models.Model):
    todo_list = models.ForeignKey(
        'TodoList', related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

