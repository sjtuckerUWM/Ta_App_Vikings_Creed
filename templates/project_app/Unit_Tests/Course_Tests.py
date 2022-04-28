
import unittest

from templates.project_app.TA import TA
from templates.project_app.course import Course
from templates.project_app.section import Section


class CourseTestCase(unittest.TestCase):
    def setup(self):
        self.c1 = Course(351, "Data Structures and Algorithms")
        self.c2 = Course(337, "System Programming")
        self.c3 = Course(361, "Intro to Software Engineering")

        self.sect1 = Section()
        self.sect2 = Section()
        self.sect3 = Section()

        t1 = TA()
        t2 = TA()
        t3 = TA()

        self.list = [t1, t2, t3]

    def testAddCourse(self):
        self.assertEqual(True, False)  # add assertion here

    def testDeleteCourse(self):
        self.assertEqual(True, False)  # add assertion here

    def testCourseAddSection(self):
        self.c1.AddSection(self, 351, self.t1, 901, "Monday: 10:00am - 11:30am")
        self.assertEqual(True, False)  # add assertion here

    def testCourseDeleteSection(self):
        self.assertEqual(True, False)  # add assertion here

    def testCourseAssignInstructor(self):
        self.assertEqual(True, False)  # add assertion here

    def testCourseAssignTA(self):
        self.c2.assignTA(self.t2)
        self.assertEqual(self.c2.containsTA(self.t2), self.sect2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
