from django.test import TestCase, Client
from proj_app.models import MyUserModel


class MyTestEditAccount(TestCase):
    client = None

    def setUp(self):
        self.client = Client()
        self.user = MyUserModel.objects.create(user_id=1, email= 'Instructor@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=0)
        self.user.save()

    def test_account_editing(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        resp1 = self.client.get('/editAccount/1/')
        resp2 = self.client.post('/editAccount/1/', {'id': '1', 'email': 'Instructor@test.com', 'name': 'Test', 'password': "passworddd", 'address': 'USA', 'phoneNum': '123-456-7890'})
        print(resp2.context) # gives no context because the page redirected to /accounts/
        self.assertEqual(resp2.url, '/accounts')
        # need to fetch the user from the database again since editAccount in driver deletes the old one and makes a new one
        self.assertEqual("passworddd", MyUserModel.objects.get(user_id=1).password,"AccountEdit is working")

    def test_account_invalid_editing(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        resp1 = self.client.get('/editAccount/1/')
        resp2 = self.client.post('/editAccount/1/', {'id': '1', 'email': 'Instructor@test.com', 'name': 'Test', 'password': "pass", 'address': 'USA', 'phoneNum': '123-456-7890'})
        self.assertEqual(resp2.context['v_password'], "Invalid, 8 or more characters")
        self.assertEqual("pass1234", MyUserModel.objects.get(user_id=1).password,"password not changed")

