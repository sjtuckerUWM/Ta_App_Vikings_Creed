from classes.instructor import Instructor
from django.test import TestCase


class TestInit(TestCase):
    def test_default(self):
        a = Instructor(1, "email@a.com", "pass1234", "John Doe", "USA", "123-456-7890")
        self.assertEqual(a.email, "email@a.com")
        self.assertEqual(a.password, "pass1234")

    def test_oneArg(self):
        a = Instructor(3, "email@a.com", "pass1234", "John Doe", "USA", "123-456-7890")
        self.assertEqual(a.name, "John Doe")
        self.assertEqual(a.address, "USA")
        self.assertEqual(a.phoneNum, "123-456-7890")


class TestInvalid(TestCase):
    def test_invalidArg(self):
        with self.assertRaises(TypeError, msg="give invalid params"):
            a = Instructor(1, 1, 1, 1)

    def test_add_too_few_args(self):
        with self.assertRaises(TypeError, msg="too few arguments"):
            a = Instructor(1, "John Doe")

    def test_add_too_many_args(self):
        with self.assertRaises(TypeError, msg="too many arguments"):
            a = Instructor(1, "", "", "", "", "", "")
