from django.test import TestCase
from todo.models import *


class TodoListTestCase(TestCase):
    def test_todo_list(self):
        TodoList.objects.create(title="Test List")
        todo_list = TodoList.objects.get(title="Test List")
        self.assertEqual(todo_list.title, "Test List")
        todo_list.delete()

        try:
            retrieved_list = TodoList.objects.get(title="Test List")
        except TodoList.DoesNotExist:
            retrieved_list = None
        self.assertEqual(retrieved_list, None)

    def test_todo_list_items(self):
        todo_list = TodoList.objects.create(title="Test")
        todo_list_item = TodoListItem.objects.create(
            todo_list=todo_list,
            title="Test Item",
            description="This is a test todo list item")

        self.assertEqual(todo_list.items.count(), 1)
        self.assertEqual(todo_list.items.first(), todo_list_item)
        todo_list.delete()
        try:
            retrieved_item = TodoListItem.objects.get(title="Test Item")
        except TodoListItem.DoesNotExist:
            retrieved_item = None
        self.assertEqual(retrieved_item, None)
