from django.test import TestCase, Client
from project_app.models import UserModel, CourseModel, SectionModel


class MyTestLogIn(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(name="Group3", password="Vikings")

    def test_LogIn_valid(self):
        response = self.client.post('/', {'name': 'Group3', 'password': 'Vikings'})
        self.assertEqual(response.url, '/homepage')

    def test_LogIn_invalid(self):
        response = self.client.post('/', {'name': 'Group3', 'password': 'Vitkings'})
        self.assertEqual(response.context['message'], 'Invalid password')

    def test_LogIn_Null_User(self):
        response = self.client.post('/', {'name': '', 'password': 'Vikings'})
        self.assertEqual(response.context['message'], 'No user name entered')

    def test_LogIn_Null_password(self):
        response = self.client.post('/', {'name': 'Group3', 'password': ''})
        self.assertEqual(response.context['message'], 'No user password entered')


class MyTestCreate(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel(name="Group3", password="Vikings")
        self.user.save()

    def test_account_valid(self):
        response = self.client.post('/', {'name': 'Group4', 'password': 'BroCops'})
        self.assertEqual(response.context['message'], 'create success')

    def test_account_invalid(self):
        response = self.client.post('/', {'name': 'Group3', 'password': 'jumper100'})
        self.assertEqual(response.context['message'], 'Already existing. Please try again.')


class MyTestCourseCreate(TestCase):

    def setUp(self):
        self.client = Client()
        self.course = CourseModel( course_id = 361, dept_code= "CS", name = "CS361", assigned_instructor= "Mr. Rock", assigned_tas = "TA apporv")
        self.course.save()

    def test_course_page(self):
        response = self.client.post('/', {'course_id': 361, 'dept_code': 'CS','name':'CS361','assigned_instructor':'Mr. Rock', 'assigned_tas':'TA apporv'}, follow = True)
        self.assertEqual(response.url, '/courseManagement/')

    def test_course_correctnes(self):
        response = self.client.post('/', {'course_id': 361, 'dept_code': 'CS','name':'CS361','assigned_instructor':'Mr. Rock', 'assigned_tas':'TA apporv'}, follow = True)
        self.assertEqual("CS361", response.context["name"])

    def test_course_invalid(self):
        response = self.client.post('/', {'course_id': 361, 'dept_code': 'CS','name':'CS361','assigned_instructor':'Mr. Rock', 'assigned_tas':'TA apporv'}, follow = True)
        self.assertFalse("", response.context["name"],"Database access problem")


class MyTestSectionCreate(TestCase):

    def setUp(self):
        self.client = Client()
        self.section = SectionModel( section_id = 361, course= "CS361", name = "801",grader= True, assigned_ta = "TA apporv")
        self.section.save()

    def test_section_page(self):
        response = self.client.post('/', {'section_id': 361, 'course': 'CS','name':'801','grader':'True', 'assigned_ta':'TA apporv'}, follow = True)
        self.assertEqual(response.url, '/sectionManagement/')

    def test_section_correctnes(self):
        response = self.client.post('/', {'section_id': 361, 'course': 'CS', 'name': '801', 'grader': 'True','assigned_ta': 'TA apporv'}, follow=True)
        self.assertEqual("801", response.context["name"])

    def test_section_invalid(self):
        response = self.client.post('/', {'section_id': 361, 'course': 'CS', 'name': '801', 'grader': 'True','assigned_ta': 'TA apporv'}, follow=True)
        self.assertFalse("", response.context["name"],"Database access problem")
        
