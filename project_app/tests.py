
from django.test import TestCase, Client
from project_app.models import User


class MyTestLogIn(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Group3", password="Vikings")

    def test_LogIn_valid(self):
        response = self.client.post('/', {'name': 'Group3', 'password': 'Vikings'})
        self.assertEqual(response.url, '/homepage')

    def test_LogIn_invalid(self):
        response = self.client.post('/', {'name': 'Group3', 'password': 'Vitkings'})
        self.assertEqual(response.context['message'], 'Invalid password')


class MyTestCreate(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User(name="Group3", password="Vikings")
        self.user.save()

    def test_account_valid(self):
        response = self.client.post('/', {'name': 'Group4', 'password': 'BroCops'})
        self.assertEqual(response.context['message'], 'create success')

    def test_account_invalid(self):
        response = self.client.post('/', {'name': 'Group3', 'password': 'jumper100'})
        self.assertEqual(response.context['message'], 'Already existing. Please try again.')
