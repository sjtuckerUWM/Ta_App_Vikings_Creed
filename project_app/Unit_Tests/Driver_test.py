import unittest
from django.test import TestCase
from project_app.Driver import Driver


# Params: id, email, password, name, address, phoneNum, role
class TestAddAccount(TestCase):
    def test_add_Instructor(self):
        a = Driver()
        self.assertEqual(a.addAccount("1", "Instructor@test.com", "pass1234", "Test", "USA", "123-456-7890", 1),
                         ["", "", "", "", "", "", ""])

    def test_add_Instructor2(self):
        a = Driver()
        self.assertEqual(a.addAccount("2", "Instructor2@test.com", "pass1234", "Test", "USA", "123-456-7890", 1),
                         ["", "", "", "", "", "", ""])

    def test_add_Instructor3(self):
        a = Driver()
        self.assertEqual(a.addAccount("3", "Instructor3@test.com", "pass1234", "Test", "USA", "123-456-7890", 1),
                         ["", "", "", "", "", "", ""])

    def test_add_TA(self):
        a = Driver()
        self.assertEqual(a.addAccount("4", "TA@test.com", "pass1234", "Test Two", "USA", "123-456-7890", 2),
                         ["", "", "", "", "", "", ""])

    def test_add_TA2(self):
        a = Driver()
        self.assertEqual(a.addAccount("5", "TA@test2.com", "pass1234", "Test Two", "USA", "123-456-7890", 2),
                         ["", "", "", "", "", "", ""])

    def test_add_TA3(self):
        a = Driver()
        self.assertEqual(a.addAccount("6", "TA@test3.com", "pass1234", "Test Two", "USA", "123-456-7890", 2),
                         ["", "", "", "", "", "", ""])

    def test_add_Supervisor(self):
        a = Driver()
        self.assertEqual(a.addAccount("7", "Supervisor@test.com", "pass1234", "Test Three", "USA", "123-456-7890", 0),
                         ["", "", "", "", "", "", ""])

    def test_add_Supervisor2(self):
        a = Driver()
        self.assertEqual(a.addAccount("8", "Supervisor2@test.com", "pass1234", "Test Three", "USA", "123-456-7890", 0),
                         ["", "", "", "", "", "", ""])

    def test_add_Supervisor3(self):
        a = Driver()
        self.assertEqual(a.addAccount("9", "Supervisor3@test.com", "pass1234", "Test Three", "USA", "123-456-7890", 0),
                         ["", "", "", "", "", "", ""])


class TestCourseList(unittest.TestCase):
    def test_emptyfields(self):
        a= Driver()


class TestAddCourse(unittest.TestCase):
    def setup(self):
        with self.assertRaises(OverflowError, msg="too many arguments"):
            a = Driver()
            a.addCourse_(123, "CS361", 801)
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Driver()
            b.addCourse_()
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Driver()
            c.addCourse_("id","CS361")
            c.addCourse_(351,361)
    def test_default(self):
        a = Driver()
        self.assertTrue(a.addCourse_(361,"CS361"))


class TestDeleteCourse(unittest.TestCase):
    def setup(self):
        with self.assertRaises(OverflowError, msg="too many arguments"):
            a = Driver()
            a.deleteCourse_(123, "CS361", 801)
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Driver()
            b.deleteCourse_()
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Driver()
            c.deleteCourse_("id")

    def test_default(self):
        a = Driver()
        self.assertTrue(a.deleteCourse_(123))


class TestaddSection(unittest.TestCase):
    def setup(self):
        with self.assertRaises(OverflowError, msg="too many arguments"):
            a = Driver()
            a.addSection_(123, "CS361", 801)
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Driver()
            b.addSection_()
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Driver()
            c.addSection_("id",123)

    def test_default(self):
        a = Driver()
        self.assertTrue(a.addSection_(361,"CS361"))


class TestDeleteSection(unittest.TestCase):
    def setup(self):
        with self.assertRaises(OverflowError, msg="too many arguments"):
            a = Driver()
            a.deletesection_(123, "CS361", 801)
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Driver()
            b.deletesection_()
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Driver()
            c.deletesection_("id",123)

    def test_default(self):
        a = Driver()
        self.assertTrue(a.deletesection_(361,"CS361"))