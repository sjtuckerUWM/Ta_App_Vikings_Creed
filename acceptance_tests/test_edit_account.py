from django.test import TestCase, Client
from proj_app.models import MyUserModel


class MyTestEditAccount(TestCase):
    client = None

    def setUp(self):
        self.client = Client()
        self.user = MyUserModel.objects.create(user_id=1, email= 'Instructor@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=1)
        self.user.save()

    def test_account_editing(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')


        response = self.client.post('editAccount/', {'user_id': '1', 'email': 'Instructor@test.com', 'name': 'Test', 'password': 'pass1234', 'address': 'USA', 'phone_number': '123-456-7890','role': '1'})
        self.user.password = 'nopass'

        self.assertEqual("nopass", self.user.password,"AccountEdit is not working")
