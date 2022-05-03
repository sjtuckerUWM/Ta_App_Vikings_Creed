import unittest
from django.test import TestCase
from classes.Driver import Driver


# Params: id, email, password, name, address, phoneNum, role
class TestAddAccount(TestCase):
    def test_add_Instructor(self):
        a = Driver()
        self.assertEqual(a.addAccount("1", "Instructor@test.com", "pass1234", "Test", "USA", "123-456-7890", 1),
                         ["", "", "", "", "", "", ""])

    def test_add_TA(self):
        a = Driver()
        self.assertEqual(a.addAccount("4", "TA@test.com", "pass1234", "Test Two", "USA", "123-456-7890", 2),
                         ["", "", "", "", "", "", ""])

    def test_add_Supervisor(self):
        a = Driver()
        self.assertEqual(a.addAccount("7", "Supervisor@test.com", "pass1234", "Test Three", "USA", "123-456-7890", 0),
                         ["", "", "", "", "", "", ""])

    def test_add_wrong_type(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="invalid argument"):
            a.addAccount(1, 1, 1, 1, 1, 1, 1, 1)

    def test_add_too_few_args(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="too few arguments"):
            a.addAccount("test")

    def test_add_too_many_args(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="too many arguments"):
            a.addAccount("", "", "", "", "", "", "", "")


class TestEditAccount(TestCase):
    def test_edit_acc(self):
        a = Driver()


# 6 strings added when done, int: courseId, string: courseName
class TestAddCourse(TestCase):
    def test_Add_Course(self):
        a = Driver()
        self.assertEqual(a.addCourse(361, "CS361"), ["", "", "", "", "", ""])

    def test_Add_Course2(self):
        a = Driver()
        self.assertEqual(a.addCourse(351, "CS351"), ["", "", "", "", "", ""])

    def test_Add_Course3(self):
        a = Driver()
        self.assertEqual(a.addCourse(337, "CS337"), ["", "", "", "", "", ""])

    def test_too_many_args_course(self):
        with self.assertRaises(OverflowError, msg="too many arguments"):
            a = Driver()
            a.addCourse_(123, "CS361", 801)

    def test_invalid_course2(self):
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Driver()
            b.addCourse_()

    def test_invalid_course3(self):
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Driver()
            c.addCourse_("id", "CS361")
            c.addCourse_(351, 361)


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