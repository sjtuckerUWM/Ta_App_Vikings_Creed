from classes.user import User
import unittest

#test for _init_() method
class TestInit1(unittest.TestCase):
    def test_instance(self):
        a = User()
        self.assertIsInstance(a, User)
    # def test_emptyfields(self):
    #     a = User()
    #     self.assertFalse(a.__class__ == TestCase)

#test for __init__(parameters)
class TestInit2(unittest.TestCase):
    def setUp(self):
        with self.assertRaises(OverflowError, msg="can't accept that many arguments"):
            d = User(1,"Vikings@gmail.com","Vikings12","Sam","13000 W Bluemound RD", "4245948394","vey2345")
        with self.assertRaises(TypeError, msg=" not enough arguments"):
            a=  d = User(1,"Vikings@gmail.com","Vikings12","Sam","13000 W Bluemound RD")
            b = d = User(1, "Vikings@gmail.com", "Vikings12", "Sam")
            c= d = User(1, "Vikings@gmail.com")

        with self.assertRaises(TypeError, msg=" invalid arguments"):
            d = User("kj", 3, 23, 45, 56, 66, 42459483)
            f = User(1, 5, "selo", "Sam", "13000 W Bluemound RD", "4245948394")
            c= User(1,"Vikings@gmail.com",45,"Sam","13000 W Bluemound RD", "4245948394")
            b = User(1, "Vikings@gmail.com", "selo34", 65, "13000 W Bluemound RD", "4245948394")
            g = User(1, "Vikings@gmail.com", 45, "Sam", "13000 W Bluemound RD", 4245948394)
            m = User(1, "", 45, "Sam", "13000 W Bluemound RD", 4245948394)


#test for getters
class Testmethods(unittest.TestCase):
    def test_getid(self):
        d = User(1,"Vikings@gmail.com","Vikings12","Sam", "13000 W Bluemound RD", "4245948394")
        self.assertEqual(1,d.getID())

    def test_getemail(self):
        d = User(1, "Vikings@gmail.com", "Vikings12", "Sam", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("Vikings@gmail.com", d.getEmail())

    def test_getpassword(self):
        d = User(1, "Vikings@gmail.com", "Vikings12", "Sam", "13000 W Bluemound RD", "4245948394")
        print(d.email + " " + str(d.userId) + " " +d.password)
        self.assertEqual("Vikings12", d.getPassword())

    def test_getname(self):
        d = User(1, "Vikings@gmail.com", "Vikings12", "Sam", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("Sam", d.getName())


    def test_getaddress(self):
        d = User(1, "Vikings@gmail.com", "Vikings12", "Sam", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("13000 W Bluemound RD", d.getAddress())

    def test_getphonenum(self):
        d = User(1, "Vikings@gmail.com", "Vikings12", "Sam", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("4245948394", d.getPhoneNum())

