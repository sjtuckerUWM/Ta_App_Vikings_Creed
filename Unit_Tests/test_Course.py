from django.test import TestCase
from proj_app.models import MyUserModel

from classes.TA import TA
from classes.instructor import Instructor
from classes.course import Course


# int: courseId, string: courseName
class Test__Init__(TestCase):
    def test_init(self):
        c = Course(351, "CS351")
        self.assertEqual(c.courseID, 351, "ID is not set")
        self.assertEqual(c.courseName, "Intro to CS", "Course Name is not set")

    def test_init2(self):
        a = Course(337, "CS337")
        self.assertEqual(a.courseID, 337, "ID is not set")
        self.assertEqual(a.courseName, "Intro to CS", "Course Name is not set")

    def test_containsTA(self):
        a = Course(351, "CS351")
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        a.assignTA(ta)
        self.assertEqual(a.containsTA(ta), True)

    def test_doesnt_containTA(self):
        a = Course(351, "CS351")
        ta1 = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        ta2 = TA("2", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        a.assignTA(ta1)
        self.assertEqual(a.containsTA(ta2), False)

    def test_setSectionList(self):
        c = Course(361, "CS361")
        c2 = Course(337, "CS337")
        t = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        c.AddSection(361, t, 801, "Monday: 10:00am - 11:30am")
        c.AddSection(361, t, 901, "Monday: 10:00am - 11:30am")
        c2.setSectionList(c.sectionList)
        self.assertEqual(c.sectionList, c2.sectionList)

    def test_setTA_list(self):
        c = Course(361, "CS361")
        c2 = Course(337, "CS337")
        t = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        t2 = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        c.assignTA(t)
        c.assignTA(t2)
        c2.setTA_list(c.TA_list)
        self.assertEqual(c.TA_list, c.TA_list)


class TestCourse(TestCase):
    def testCourseAssignInstructor(self):
        c1 = Course(337, "CS337")
        inst = Instructor("1", "Instructor@test.com", "pass1234", "Test Inst", "USA", "123-456-7890")
        c1.assignInstructor(inst.getID())
        self.assertEqual(c1.instructorId, inst.getID())

    def testCourseAssignTA(self):
        c1 = Course(337, "CS337")
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        c1.assignTA(ta)
        self.assertEqual(c1.TA_list[0], ta)


class TestAddSection(TestCase):
    def test_Course_Add_Section(self):
        c = Course(361, "CS361")
        t = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        self.assertEqual(c.AddSection(361, t, 901, "Monday: 10:00am - 11:30am"), True)

    def test_Course_Add_Section2(self):
        c = Course(337, "CS337")
        t = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        self.assertEqual(c.AddSection(337, t, 801, "Monday: 10:00am - 11:30am"), True)

    def test_too_many_args(self):
        with self.assertRaises(TypeError, msg="too many arguments"):
            a = Course()
            a.AddSection(123, "CS361", 801)

    def test_no_args(self):
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Course()
            b.AddSection()

    def test_invalid_args(self):
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Course()
            c.AddSection("id", 123)


class TestDeleteSection(TestCase):
    def test_Course_Delete_Section(self):
        c1 = Course(361, "CS361")
        t = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        c1.AddSection(361, t, 801, "Monday: 10:00am - 11:30am")
        self.assertEqual(c1.DeleteSection(801), True)

    def test_Course_Delete_Section2(self):
        c1 = Course(337, "CS337")
        t = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        c1.AddSection(337, t, 801, "Monday: 10:00am - 11:30am")
        self.assertEqual(c1.DeleteSection(801), True)

    def test_too_many_args(self):
        with self.assertRaises(TypeError, msg="too many arguments"):
            a = Course()
            a.DeleteSection(123, "CS361", 801)

    def test_no_args(self):
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Course()
            b.DeleteSection()

    def test_invalid_args(self):
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Course()
            c.DeleteSection("id", 123)
