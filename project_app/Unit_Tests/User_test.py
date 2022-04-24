from project_app.user import user
import unittest

#test for _init_() method
class TestInit1(unittest.TestCase):
    def test_instance(self):
        a = user()
        self.assertIsInstance(user,a._init_())
    def test_emptyfields(self):
        a= user()
        self.assertFalse(2, a._init_())

#test for __init__(parameters)
class TestInit2(unittest.TestCase):
    def setUp(self):
        with self.assertRaises(OverflowError, msg="can't accept that many arguments"):
            d = user(1,"Vikings@gmail.com","Vikings12","Sam", "Tucker","13000 W Bluemound RD", "4245948394","vey2345")
        with self.assertRaises(TypeError, msg=" not enough arguments"):
            a=  d = user(1,"Vikings@gmail.com","Vikings12","Sam", "Tucker","13000 W Bluemound RD")
            b = d = user(1, "Vikings@gmail.com", "Vikings12", "Sam")
            c= d = user(1, "Vikings@gmail.com")

        with self.assertRaises(TypeError, msg=" invalid arguments"):
            d = user("kj", 3, 23, 45, 56, 66, 42459483)
            f = user(1, 5, "selo", "Sam", "Tucker", "13000 W Bluemound RD", "4245948394")
            c= user(1,"Vikings@gmail.com",45,"Sam", "Tucker","13000 W Bluemound RD", "4245948394")
            b = user(1, "Vikings@gmail.com", "selo34", 65, "Tucker", "13000 W Bluemound RD", "4245948394")
            g = user(1, "Vikings@gmail.com", 45, "Sam", "Tucker", "13000 W Bluemound RD", 4245948394)


#test for getters
class Testmethods(unittest.TestCase):
    def test_getid(self):
        d = user(1,"Vikings@gmail.com","Vikings12","Sam", "Tucker","13000 W Bluemound RD", "4245948394")
        self.assertEqual(1,d.getid_())

    def test_getemail(self):
        d = user(1, "Vikings@gmail.com", "Vikings12", "Sam", "Tucker", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("Vikings@gmail.com", d.getemail_())

    def test_getpassword(self):
        d = user(1, "Vikings@gmail.com", "Vikings12", "Sam", "Tucker", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("Vikings12", d.getpassword_())

    def test_getfname(self):
        d = user(1, "Vikings@gmail.com", "Vikings12", "Sam", "Tucker", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("Sam", d.getfname_())

    def test_getlname(self):
        d = user(1, "Vikings@gmail.com", "Vikings12", "Sam", "Tucker", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("Tucker", d.getlname_())

    def test_getaddress(self):
        d = user(1, "Vikings@gmail.com", "Vikings12", "Sam", "Tucker", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("13000 W Bluemound RD", d.getaddress_())

    def test_getphonenum(self):
        d = user(1, "Vikings@gmail.com", "Vikings12", "Sam", "Tucker", "13000 W Bluemound RD", "4245948394")
        self.assertEqual("4245948394", d.getphonenum_())

