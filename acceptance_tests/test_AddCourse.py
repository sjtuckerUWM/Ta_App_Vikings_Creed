from django.test import TestCase, Client
from proj_app.models import CourseModel, MyUserModel


class MyTestAddCourse(TestCase):

    def setUp(self):
        self.client = Client()
        self.course = CourseModel.objects.create(course_id=2,  dept_code="COMP SCI", name= " Intro to Programming")
        self.user = MyUserModel.objects.create(user_id=1, email='Instructor@test.com', password='pass1234',
                                               name='Test', address='USA', phone_number='123-456-7890', role=1)

    def test_course_adding(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        self.course2 = CourseModel.objects.create(course_id=3, dept_code="COMP SCI", name=" Intro to AI")
        resp = self.client.post('addCourse/', {'id': self.course2.course_id, 'dep': self.course2.dept_code,
                                               'name': self.course2.name})
        courses = CourseModel.objects.all()

        self.assertEqual(len(courses), 2)

