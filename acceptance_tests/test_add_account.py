from django.test import TestCase, Client
from proj_app.models import MyUserModel


class MyTestAddAccount(TestCase):


    def setUp(self):
        self.client = Client()
        self.user = MyUserModel.objects.create(user_id=1, email= 'Instructor@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=1)



    def test_account_invalid(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')
        resp = self.client.post('/addAccount/', {'id': -4, 'email': self.user.email, 'password': self.user.password,'name': self.user.name, 'address': self.user.address,'phoneNum': self.user.phone_number, 'role': self.user.role}, follow=True)
        self.assertEqual(resp.context["v_id"], "Invalid, integer between 0 and 9999" )



    def test_account_adding(self):

        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')


        # self.user2 = MyUserModel.objects.create(user_id=2, email='ta1@uwm.edu', password='pass1234', name='Apoorv', address='USA',phone_number='123-456-7890', role=2)
        resp = self.client.post('/addAccount/', {'id': 5, 'email': "ta1@uwm.edu", 'password': " pass1234",'name': "Odin", 'address': "USA",'phoneNum': "414-630-8598", 'role': 2}, follow=True)
        #self.assertEqual(resp.url, "/accounts")
        users = MyUserModel.objects.all()
        self.assertEqual(len(users),2)



