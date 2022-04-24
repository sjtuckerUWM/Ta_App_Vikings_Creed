from project_app.supervisor import Supervisor

import unittest


class TestInit(unittest.TestCase):

  def test_default(self):
    a = Supervisor()
    self.assertEqual(a, Supervisor(1, "email@a.com", "pass", "John Doe", "USA", "123-456-7890"))
  def test_oneArg(self):
    a = Supervisor(3)
    self.assertEqual(a, Supervisor(3, "email@a.com", "pass", "John Doe", "USA", "123-456-7890"))
  def test_twoArg(self):
    a = Supervisor(3, "hello@gmail.com")
    self.assertEqual(a, Supervisor(3, "hello@gmail.com", "pass", "John Doe", "USA", "123-456-7890"))
  def test_invalidArg(self):
      with self.assertRaises(ValueError, msg="give invalid params"):
          a = Supervisor("hi", "hello@gmail.com", 3, 2)
