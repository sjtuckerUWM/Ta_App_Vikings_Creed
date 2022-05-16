from django.test import TestCase, Client
from proj_app.models import MyUserModel

class MyTestDeleteAccount(TestCase):
    client = None

    def setUp(self):
        self.client = Client()
        self.user = MyUserModel.objects.create(user_id=1,email= "Instructor@test.com", password="pass1234", name="Test", address="USA", phone_number="123-456-7890", role=1)
        self.user.save()

    def test_account_Delete(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        resp= self.client.post(f'/deleteAccount/{self.user.user_id}/')
        self.assertEqual(resp.url,'/accounts')
        
