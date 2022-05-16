from django.test import TestCase

from classes.TA import TA
from classes.section import Section


class Test__Init__(TestCase):
    def test__init(self):
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        s = Section(ta, 801, "Mon-Wed EMS180 10-11am")
        self.assertEqual(s.TA, ta)
        self.assertEqual(s.sectNum, 801)

    def test__init2(self):
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        s = Section(ta, 901, "Mon-Wed EMS180 10-11am")
        self.assertEqual(s.TA, ta)
        self.assertEqual(s.sectNum, 901)
        self.assertEqual(s.meetingInfo, "Mon-Wed EMS180 10-11am")

    def test_too_many_args(self):
        with self.assertRaises(TypeError, msg="too many arguments"):
            ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
            a = Section(ta, 901, "meeting place", 1)

    def test_no_args(self):
        with self.assertRaises(TypeError, msg=" no argument"):
            b = Section()

    def test_invalid_args(self):
        with self.assertRaises(TypeError, msg=" invalid arguments"):
            c = Section("id", 123)


class TestSetters(TestCase):
    def test_setTA(self):
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        ta2 = TA("2", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        s = Section(ta, 901, "Mon-Wed EMS180 10-11am")
        s.setTA(ta2)
        self.assertEqual(s.TA, ta2)

    def test_setCourseNum(self):
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        s = Section(ta, 901, "Mon-Wed EMS180 10-11am")
        s.setCourseNum(361)
        self.assertEqual(s.courseNum, 361)

    def test_setLabStatus(self):
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        s = Section(ta, 901, "Mon-Wed EMS180 10-11am")
        s.setLabStatus(True)
        self.assertEqual(s.hasLab, True)

    def test_setSectionNum(self):
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        s = Section(ta, 901, "Mon-Wed EMS180 10-11am")
        s.setSectionNum(801)
        self.assertEqual(s.sectNum, 801)

    def test_setMeetingPlace(self):
        ta = TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
        s = Section(ta, 901, "Mon-Wed EMS180 10-11am")
        s.setMeetingPlace("Milwaukee")
        self.assertEqual(s.meetingInfo, "Milwaukee")
