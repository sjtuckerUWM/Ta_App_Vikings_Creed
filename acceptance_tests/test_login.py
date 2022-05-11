from django.test import TestCase, Client
from proj_app.models import MyUserModel


class MyTestLogIn(TestCase):
    def setUp(self):

        self.client = Client()
        self.user = MyUserModel.objects.create(name="", email="Group3", password="Vikings", address="", role=0)

    def test_LogIn_valid(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        print(response.context)
        self.assertEqual(response.url, '/home/')

    def test_LogIn_invalid(self):
        response = self.client.post('/', {'email': 'Group3', 'password': 'Vitkings'})
        self.assertEqual(response.context['message'], 'bad password')

    def test_LogIn_Null_User(self):
        response = self.client.post('/', {'email': '', 'password': 'Vikings'})
        self.assertEqual(response.context['message'], 'email is not registered')

    def test_LogIn_Null_password(self):
        response = self.client.post('/', {'email': 'Group3', 'password': ''})
        self.assertEqual(response.context['message'], 'bad password')

