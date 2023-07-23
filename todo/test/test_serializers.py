from django.test import TestCase
from todo import serializers


class ToDoListTestCase(TestCase):
    def test_todo_list_create(self):
        data = {
            'title': 'Test List',
            'items': [
                {
                    'title': 'Test Item 1',
                    'description': 'This is test item 1'
                },
                {
                    'title': 'Test Item 2',
                    'description': 'This is test item 2'
                }
            ]
        }

        serializer = serializers.TodoList(data=data)
        self.assertTrue(serializer.is_valid())

        todo_list = serializer.save()

        self.assertEqual(todo_list.title, 'Test List')
        self.assertEqual(todo_list.items.count(), 2)
