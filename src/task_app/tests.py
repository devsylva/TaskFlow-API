from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task, Category, Tag


# Create your tests here.
User = get_user_model()

class TaskModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email='testemail@gmail.com',
            password="Password123"
        )
        self.category = Category.objects.create(
            name="Study",
            user=self.user
        )
        self.tag = Tag.objects.create(
            name="tag 1",
            user=self.user
        )

    def test_create_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Task title",
            description="This is a test task",
            category=self.category,
            tag=self.tag
        )

        self.assertEqual(task.title, "Task title")
        self.assertEqual(task.user, self.user)