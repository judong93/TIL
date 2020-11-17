from django.test import TestCase
from accounts.models import User

# Create your tests here.
class TodoTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='password')
  
    def test_todo_index(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/todos/')


        self.client.login(username='testuser', password='password')
        response = self.client.get('/todos/')
        self.assertTemplateUsed(response, 'todos/index.html')

    def test_todo_create_get(self):
        self.client.login(username='testuser', password='password')
        # todos 경로로 요청한다.
        response = self.client.get('/todos/create/')
        # todos/form.html이 렌더링 되었는지 확인한다.
        self.assertTemplateUsed(response, 'todos/form.html')
        self.assertEqual(response.status_code, 200)

    def test_todo_create_post(self):
        pass

