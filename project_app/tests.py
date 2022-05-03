from django.test import TestCase, Client
from project_app.models import UserModel, CourseModel, SectionModel


class MyTestLogIn(TestCase):
    def setUp(self):
        # self.user = UserModel.objects.create(name="", email="Group3", password="Vikings", address="", role=0)
        self.client = Client()
        self.user = UserModel(name="", email="Group3", password="Vikings", address="", role=0)
        self.user.save()

    def test_LogIn_valid(self):
        response = self.client.post('/', {'email': 'Group3', 'password': 'Vikings'})
        self.assertEqual(response.url,'/home/')

    def test_LogIn_invalid(self):
        response = self.client.post('/', {'email': 'Group3', 'password': 'Vitkings'})
        self.assertEqual(response.context['message'], 'bad password')

    def test_LogIn_Null_User(self):
        response = self.client.post('/', {'email': '', 'password': 'Vikings'})
        self.assertEqual(response.context['message'], 'email is not registered')

    def test_LogIn_Null_password(self):
        response = self.client.post('/', {'email': 'Group3', 'password': ''})
        self.assertEqual(response.context['message'], 'bad password')


class MyTestAddAccount(TestCase):


    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create(user_id=1, email= 'Instructor@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=1)


    def test_account_valid(self):

        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        print(response.context)
        self.assertEqual(response.url,'/accounts/')
        resp = self.client.get('manageCourse/')
       # self.assertEqual(resp.context["email"], "Instructor@test.com")

    def test_account_invalid(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')
       # self.assertEqual(response.context["name"],"Test", "Wrong name in the database")

        #self.assertEqual(response.context["email"], "Instructor@test.com", "Wrong email in the database")


    def test_account_precise(self):
        response = self.client.post("/",{'email': self.user.email, 'password': self.user.password})
        self.assertIn(response.url, "/home/")
        #for j in response.context['home/courseManagement.html/']:
            #self.assertIn(j, "1", "user has extra paramater" )
            #self.assertIn(j, "Instructor@test.com", "user has extra paramater")
            #self.assertIn(j, "Test", "user has extra paramater")
            #self.assertIn(j, "pass1234'", "user has extra paramater")
            #self.assertIn(j, "USA", "user has extra paramater")
            #self.assertIn(j, "123-456-7890", "user has extra paramater")
            #self.assertIn(j, 1, "user has extra paramater")

    def test_account_adding(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')
        self.user2 = UserModel(user_id=2, email= 'TA@test.com', password='pass1234', name='Apoorv', address='USA', phone_number='123-456-7890', role=2)

        response = self.client.post('addAccount/', {'user_id':self.user2.user_id, 'email': self.user2.email, 'password':self.user2.password,'name':self.user2.name, 'address':self.user2.address, 'phone_number':self.user2.phone_number, 'role':self.user2.role})

        self.assertEqual(response.context['message'])



class MyTestEditAccount(TestCase):
    client = None

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create(user_id=1, email= 'Instructor@test.com', password='pass1234', name='Test', address='USA', phone_number='123-456-7890', role=1)
        self.user.save()

    def test_account_editing(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')
        session = self.client.session

        response = self.client.post('/', {'user_id': '1', 'email': 'Instructor@test.com', 'name': 'Test', 'password': 'pass1234', 'address': 'USA', 'phone_number': '123-456-7890','role': '1'})
        session['password'] = 'nopass'
        session.save()
        r = self.client.get('manageCourses/')
       # self.assertEqual("nopass", r.context["password"],"AccountEdit is not working")


class MyTestDeleteAccount(TestCase):
    client = None

    def setUp(self):
        self.client = Client()
        user = UserModel.objects.create(user_id=1,email= "Instructor@test.com", password="pass1234", name="Test", address="USA", phone_number="123-456-7890", role=1)
        user.save()

    def test_account_Delete(self):
        response = self.client.post('/', {'email': self.user.email, 'password': self.user.password})
        self.assertEqual(response.url, '/home/')

        UserModel.objects.get(user_id=1).delete()
        response = self.client.get('manageCourse/')







class MyTestCourseCreate(TestCase):

    def setUp(self):
        self.client = Client()
        self.course = CourseModel( course_id = 361, dept_code= "CS", name = "CS361", assigned_instructor= "Mr. Rock", assigned_tas = "TA apporv")
        self.course.save()

    def test_course_page(self):
        response = self.client.post('/', {'course_id': 361, 'dept_code': 'CS','name':'CS361','assigned_instructor':'Mr. Rock', 'assigned_tas':'TA apporv'}, follow = True)
        self.assertEqual(response.url, 'home/courseManagement.html/')

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
        


