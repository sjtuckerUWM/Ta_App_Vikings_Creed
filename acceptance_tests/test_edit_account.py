from django.test import TestCase, Client
from proj_app.models import MyUserModel


class MyTestEditAccount(TestCase):
    client = None

    def setUp(self):
        self.client = Client()
        self.user = MyUserModel.objects.create(user_id= 2, email= 'Instructor@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=1)
        self.user.save()

    def test_account_editing(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        resp = self.client.post(f'/editAccount/{self.user.user_id}', {'id':self.user.user_id, 'email': "Instructor@uwm.edu", 'password': self.user.password,'name': self.user.name, 'address': self.user.address,'phoneNum': self.user.phone_number, 'role': self.user.role}, follow=True)
        #  self.assertEqual(resp.context['v_email'], "email doesn't match")

        self.assertEqual("Instructor@uwm.edu",self.user.email ,"email doesn't match")


    def test_account_editing_invalid(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')


        resp = self.client.post(f'/editAccount/{self.user.user_id}', {'role':2 }, follow=True)
        self.assertEqual(resp.context['role'], "Instructor", "can't change the role")

        #self.assertEqual("Instructor@uwm.edu","Instructor@uwm.edu" ,"email doesn't match")
