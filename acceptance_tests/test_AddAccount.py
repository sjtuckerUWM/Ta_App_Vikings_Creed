from django.test import TestCase, Client
from proj_app.models import MyUserModel


class TestAddAccount(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = MyUserModel.objects.create(user_id=1, email= 'Instructor@test.com', password='pass1234',
                                               name='Test', address='USA', phone_number='123-456-7890', role=1)

    def test_account_valid(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')
        resp = self.client.get('manageCourse/')
        self.assertEqual(self.user.email, "Instructor@test.com")

    def test_account_invalid(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')
        resp = self.client.post('addAccount/', {'user_id': 2, 'email': self.user.email, 'password': self.user.password,
                                                'name': self.user.name, 'address': self.user.address,
                                                'phone_number': self.user.phone_number, 'role': self.user.role})

        self.assertEqual(self.user.name, "Test", "Wrong name in the database")

        self.assertEqual(self.user.user_id, 1, "Wrong email in the database")

    def test_account_precise(self):
        response = self.client.post("/", {'email': self.user.email, 'password': self.user.password})
        self.assertIn(response.url, "/home/")

    def test_account_adding(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        self.user2 = MyUserModel.objects.create(user_id=2, email='', password='pass1234', name='Apoorv', address='USA',
                                                phone_number='123-456-7890', role=2)

        resp = self.client.post('addAccount/', {'user_id': 2, 'email': self.user2.email,
                                                'password': self.user2.password, 'name': self.user2.name,
                                                'address': self.user2.address, 'phone_number': self.user2.phone_number,
                                                'role': self.user2.role})
        print(resp.context)

        users = MyUserModel.objects.all()

        self.assertEqual(len(users), 2)
