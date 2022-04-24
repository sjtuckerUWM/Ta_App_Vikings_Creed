
from project_app.Driver import Driver
import unittest



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