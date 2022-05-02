from django.test import TestCase
from project_app.Driver import Driver


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
    def test_edit_Instructor(self):
        a = Driver()
        a.addAccount("1", "Instructor@test.com", "pass1234", "test", "USA", "123-456-7890", 1)
        self.assertEqual(a.editAccount("1", "2", "Instructor@test.com", "pass1234", "test", "USA", "123-456-7890", 1),
                         ["", "", "", "", "", "", ""])

    def test_edit_TA(self):
        a = Driver()
        a.addAccount("3", "TA@test.com", "pass1234", "test", "USA", "123-456-7890", 2)
        self.assertEqual(a.editAccount("3", "4", "TA@test.com", "pass1234", "test", "USA", "123-456-7890", 2),
                         ["", "", "", "", "", "", ""])

    def test_edit_Supervisor(self):
        a = Driver()
        a.addAccount("5", "Supervisor@test.com", "pass1234", "test", "USA", "123-456-7890", 0)
        self.assertEqual(a.editAccount("5", "6", "Supervisor@test.com", "pass1234", "test", "USA", "123-456-7890", 0),
                         ["", "", "", "", "", "", ""])

    def test_add_wrong_type(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="invalid argument"):
            a.editAccount(1, 1, 1, 1, 1, 1, 1, 1, 1)

    def test_add_too_few_args(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="too few arguments"):
            a.editAccount("test")

    def test_add_too_many_args(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="too many arguments"):
            a.editAccount("", "", "", "", "", "", "", "", "", 0)


class TestDeleteAccount(TestCase):
    def test_delete_Instructor(self):
        a = Driver()
        a.addAccount("24", "Instructor@test.com", "pass1234", "test", "USA", "123-456-7890", 1)
        self.assertIsNone(a.deleteAccount(24))

    def test_delete_TA(self):
        a = Driver()
        a.addAccount("3", "TA@test.com", "pass1234", "test", "USA", "123-456-7890", 2)
        self.assertIsNone(a.deleteAccount(3))

    def test_delete_Supervisor(self):
        a = Driver()
        a.addAccount("5", "Supervisor@test.com", "pass1234", "test", "USA", "123-456-7890", 0)
        self.assertIsNone(a.deleteAccount(5))

    def test_delete_wrong_type(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="invalid argument"):
            a.editAccount(1, 1)

    def test_delete_too_few_args(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="too few arguments"):
            a.editAccount()

    def test_delete_too_many_args(self):
        a = Driver()
        with self.assertRaises(TypeError, msg="too many arguments"):
            a.editAccount("1", "1")


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


class TestDeleteCourse(TestCase):
    def test_delete_course1(self):
        a = Driver()
        a.addCourse(351, "CS351")
        self.assertIsNone(a.deleteCourse(351))

    def test_delete_course2(self):
        a = Driver()
        a.addCourse(361, "CS361")
        self.assertIsNone(a.deleteCourse(361))

    def test_delete_course3(self):
        a = Driver()
        a.addCourse(337, "CS337")
        self.assertIsNone(a.deleteCourse(337))

    def test_too_many_args(self):
        with self.assertRaises(OverflowError, msg="too many arguments"):
            a = Driver()
            a.deleteCourse_(123, "CS361", 801)

    def test_no_args(self):
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Driver()
            b.deleteCourse_()

    def test_invalid_args(self):
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Driver()
            c.deleteCourse_("id")


class TestAddSection(TestCase):
    def test_add_section1(self):
        a = Driver()
        self.assertEqual(a.addSection(361, "CS361"))

    def test_add_section2(self):
        a = Driver()
        self.assertEqual(a.addSection(361, "CS361"))

    def test_add_section3(self):
        a = Driver()
        self.assertEqual(a.addSection(361, "CS361"))

    def test_too_many_args(self):
        with self.assertRaises(OverflowError, msg="too many arguments"):
            a = Driver()
            a.addSection(123, "CS361", 801)

    def test_no_args(self):
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Driver()
            b.addSection()

    def test_invalid_args(self):
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Driver()
            c.addSection("id", 123)


class TestDeleteSection(TestCase):
    def test_default(self):
        a = Driver()
        self.assertTrue(a.deletesection(361, "CS361"))

    def test_default(self):
        a = Driver()
        self.assertTrue(a.deletesection(361, "CS361"))

    def test_default(self):
        a = Driver()
        self.assertTrue(a.deletesection(361, "CS361"))

    def test_too_many_args(self):
        with self.assertRaises(OverflowError, msg="too many arguments"):
            a = Driver()
            a.deletesection(123, "CS361", 801)

    def test_no_args(self):
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Driver()
            b.deletesection()

    def test_invalid_args(self):
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Driver()
            c.deletesection("id", 123)
