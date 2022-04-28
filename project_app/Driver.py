from project_app.supervisor import Supervisor
from project_app.instructor import Instructor
from project_app.TA import TA
from project_app.course import Course
from project_app.section import Section
from project_app.models import UserModel, CourseModel, SectionModel
import re

class Driver(object):
    def __init__(self, currentAccount=None):
        self.currentAccount = currentAccount
        self.accountList = {}
        self.courseList = {}
        # self.addAccount(1, "email@a.com", "pass", "Test User", "USA", "123-456-7890", 0)
        self.fillAccounts()
        # to see if logIn works VVV
        # self.addAccount(1, "email@a.com", "pass", "Test User", "USA", "123-456-7890", 0)

    def getCurrentAccount(self):
        return self.currentAccount

    def fillAccounts(self):

        # things = UserModel.objects.iterator(100
        things = list(UserModel.objects.all())

        for entry in things:
            print(entry.email)
            if (entry.role == 0):
                self.accountList[entry.email] = (Supervisor(entry.user_id, entry.email, entry.password, entry.name, entry.address, entry.phone_number))

            elif (entry.role == 1):
                self.accountList[entry.email] = (Instructor(entry.user_id, entry.email, entry.password, entry.name, entry.address, entry.phone_number))
            elif (entry.role == 2):
                self.accountList[entry.email] = (TA(entry.user_id, entry.email, entry.password, entry.name, entry.address, entry.phone_number))

    def logIn(self, email, password):
        # if self.currentAccount != None: return RuntimeError
        try:
            m = UserModel.objects.get(email=email)
            if UserModel.objects.get(email=email).password == password:
                self.currentAccount = self.accountList[email]
                return 2
            return 1
        except:
            return 0


    def addAccount(self, id, email, password, name, address, phoneNum, role):
        a = ["","","","",""]
        if (re.search("+[0-9]]", id)==None) or int(id) > 99999 or int(id) < 0: a[0] = "Invalid, integer between 0 and 99999"
        if (re.search("^(+\w@+[0-9a-z]\.)", email) == None) or (len(str(email))>99): a[1] =  "Invalid"
        if (len(str(password))<8) or (len(str(password))>19): a[2] =  "Invalid, 8 or more characters"
        if (re.search("\D", name) == None) or (len(str(name))>49): a[3] =  "Invalid, can't contain digits"
        if (len(str(address))<3) or (len(str(address))>99): a[4] =  "Invalid, length should be >= 3 and < 100"
        if (re.search("({3}[0-9]\-{3}[0-9]\-{4}[0-9])|({10}[0-9])", phoneNum) == None): a[5] =  "Invalid, Format should be: \"123-456-7890\" OR \"1234567890\""







        if(role == 0) :
            self.accountList[email] = (Supervisor(id, email, password, name, address, phoneNum))

        elif(role == 1) :
            self.accountList[email] = (Instructor(id, email, password, name, address, phoneNum))
        elif (role == 2):
            self.accountList[email] = (TA(id, email, password, name, address, phoneNum))

        added = UserModel(id, name, email, password,  address, phoneNum, role)
        added.save()
        return a

    def deleteAccount(self, accountIndex):
        UserModel.objects.get(user_id=self.accountList.__getitem__(accountIndex)).delete()
        UserModel.save()
        self.accountList.pop(accountIndex)

    def addCourse(self, courseid, coursename):
        # Precondition: Course parameters are valid
        # Postcondition: Course has been added to the courses list
        pass

    def deleteCourse(self,  courseIndex):
        pass



