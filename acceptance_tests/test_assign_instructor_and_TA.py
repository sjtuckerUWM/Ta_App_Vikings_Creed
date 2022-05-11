from django.test import TestCase, Client
from proj_app.models import CourseModel, MyUserModel


class MyTestAssignCourse(TestCase):

    def setUp(self):
        self.client = Client()
        self.course = CourseModel.objects.create(course_id=2, dept_code="COMP SCI", name=" Intro to Programming")
        self.user = MyUserModel.objects.create(user_id=0, email='Instructor@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=0)

    def test_no_Instructor(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        resp = self.client.get('assignToCourse/', {'instructor': '', 'tas': ''})
        # self.assertEqual(resp.context['error'], 'There is no instructor to assign')
        instructors = list(MyUserModel.objects.filter(role=1).all())
        self.assertEqual(len(instructors),0);


    def test_no_TA(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        resp = self.client.get('assignToCourse/', {'instructor': '', 'tas': ''})
        tas = list(MyUserModel.objects.filter(role=2).all())
        # self.assertEqual(resp.context['error'], 'There is no TA to assign')
        self.assertEqual(len(tas), 0);

    def test_course_assigningInstructor(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        self.user1 = MyUserModel.objects.create(user_id=1, email='Instructor@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=1)
        self.user2 = MyUserModel.objects.create(user_id=2, email='TA1@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=2)
        self.user3 = MyUserModel.objects.create(user_id=3, email='TA2@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=2)

        tas = list(MyUserModel.objects.filter(role=2).all())

        resp = self.client.post('assignToCourse/', {'instructor': self.user, 'tas': tas})
        # self.assertEqual(resp.context['instructorList'],self.user1, "Problem with assigning Instructor")
