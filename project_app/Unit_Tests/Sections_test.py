import unittest
from project_app.TA import TA
from project_app.section import Section


class MyTestCase(unittest.TestCase):
    def setUp(self):
        t1 = TA()
        t2 = TA()

        self.t1.setName("John")
        self.t2.setName("Sally")

        self.sect1 = Section(t1, 801, "Library")
        self.sect2 = Section(t2, 901, "remote")

    def test_creation(self):
        self.assertEqual(self.sect1.getCourseNum(), 801)
        self.assertEqual(self.sect1.getMeetingPlace(), "Library")

        self.assertEqual(self.sect2.getCourseNum(), 901)
        self.assertEqual(self.sect2.getMeetingPlace(), "remote")


if __name__ == '__main__':
    unittest.main()
