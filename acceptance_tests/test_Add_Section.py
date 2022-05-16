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

        self.client.post('/addCourse/', {'id': 3, 'dep': "COMP SCI", 'name': " Intro to AI"})

        resp = self.client.post(f'/addSection/{self.section.section_id}', {'id': self.section.section_id})
        self.assertEqual(resp.url, '/addSection/801/')

        sections = SectionModel.objects.all()
        self.assertEqual(len(sections), 1)

    def test_course_invalid_add(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        resp = self.client.post(f'/addSection/{self.section.section_id}', {'id': -3}, follow=True)
        sections = SectionModel.objects.all()

        self.assertEqual(len(sections), 1)
