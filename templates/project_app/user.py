# User
# __init__(self)
# __init__(self, id, email, password, fName, lName, address, phoneNum)
# id: int
# email: string
# password: string
# name: string
# address: string
# phone: string
# role: int
# getters/setters: accesses and modifies data within user

class User(object):


    def __init__(self, userId=1, email="email@a.com", password="pass", name="John Doe", address="USA", phoneNum="123-456-7890"):
        self.userId = userId
        self.email = email
        self.password = password
        self.name = name
        self.address = address
        self.phoneNum = phoneNum

    def getID(self):
        return self.userId

    def setID(self, userId):
        self.userId = userId

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getPhoneNum(self):
        return self.phoneNum

    def setPhoneNum(self, phoneNum):
        self.phoneNum = phoneNum
