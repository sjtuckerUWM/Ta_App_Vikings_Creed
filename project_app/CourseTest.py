from django.test import TestCase, Client
from project_app.models import UserModel, CourseModel, SectionModel


class MyTestAddCourse(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = UserModel(user_id=1, name="Mr. Rock", email="rock@uwm.edu", password="GoTeam3",
                               address="2131 North state road", phone_number="345-345-1345", role=1)
        self.user1.save()
        self.user2 = UserModel(user_id=2, name="Apporv", email="apporv@uwm.edu", password="GoTeam3",
                               address="2145 South State road", phone_number="345-256-7985", role=2)
        self.user2.save()
        self.course = CourseModel(course_id=361, dept_code="CS", course_num="361", name="CS361",
                                  assigned_instructor=self.user1.name, assigned_tas=self.user2.name)
        self.course.save()

    def test_course_page(self):
        response = self.client.post('/', {'course_id': 361, 'dept_code': 'CS', 'course_num': "361", 'name': 'CS361',
                                          'assigned_instructor': 'Mr. Rock', 'assigned_tas': 'Apporv'}, follow=True)
        self.assertEqual(response.url, '/courseManagement/')

    def test_course_correctness(self):
        response = self.client.post('/', {'course_id': 361, 'dept_code': 'CS', 'course_num': "361", 'name': 'CS361',
                                          'assigned_instructor': 'Mr. Rock', 'assigned_tas': 'TA apporv'}, follow=True)
        rightName = response.context["dept_code"]+response.context["course_num"]
        self.assertEqual(rightName, response.context["name"])

    def test_course_invalid(self):
        response = self.client.post('/', {'course_id': 361, 'dept_code': 'CS', 'course_num': "361", 'name': '',
                                          'assigned_instructor': 'Mr. Rock', 'assigned_tas': 'TA apporv'}, follow=True)
        self.assertFalse("", response.context["name"], "Database access problem")
