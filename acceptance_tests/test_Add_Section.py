from django.test import TestCase, Client
from proj_app.models import CourseModel, MyUserModel, SectionModel


class MyTestAddSection(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = CourseModel.objects.create(course_id=2,  dept_code="COMP SCI", name=" Intro to Programming")
        self.section = SectionModel.objects.create(course_id=2, section_id=801)
        self.user = MyUserModel.objects.create(user_id=1, email='Instructor@test.com', password='pass1234', name='Test',
                                               address='USA', phone_number='123-456-7890', role=1)

    def test_section_adding(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        self.course2 = CourseModel.objects.create(course_id=3, dept_code="COMP SCI", name=" Intro to AI")
        self.section2 = SectionModel.objects.create(course_id=3, section_id=901)

        resp = self.client.post(f'/addSection/{self.section2.section_id}', {'id': self.section2.section_id})
        self.assertEqual(resp.url, '/addSection/901/')

        sections = SectionModel.objects.all()

        self.assertEqual(len(sections), 2)

    def test_course_invalid_add(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        resp = self.client.post(f'/addSection/', {'id': -3}, follow=True)
        sections = SectionModel.objects.all()

        # there should be only one item from the setup
        self.assertEqual(len(sections), 1)
