from project_app.supervisor import Supervisor
from project_app.instructor import Instructor
from project_app.TA import TA
from project_app.course import Course
from project_app.section import Section
from models import User, Course, Section

class Driver(object):
    def __init__(self):
        self.currentAccount = None
        self.accountList = []
        self.courseList = []
        self.fillAccounts()

        pass

    def fillAccounts(self):

        things = list(map(str, User.objects))
        for entry in things:
            if (entry.role is 0):
                self.accountList.append(Supervisor(entry.id, entry.email, entry.password, entry.name, entry.address, entry.phoneNum))

            elif (entry.role is 1):
                self.accountList.append(Instructor(entry.id, entry.email, entry.password, entry.name, entry.address, entry.phoneNum))
            elif (entry.role is 2):
                self.accountList.append(TA(entry.id, entry.email, entry.password, entry.name, entry.address, entry.phoneNum))

    def logIn(self, email, password):
        if User.email.__contains__(email):
            if User.objects.get(email=email).password is password:
                return 2
            return 1
        return 0

    def addAccount(self, id, email, password, name, address, phoneNum, role):
        if(role is 0) :
            self.accountList.append(Supervisor(id, email, password, name, address, phoneNum))

        elif(role is 1) :
            self.accountList.append(Instructor(id, email, password, name, address, phoneNum))
        elif (role is 2):
            self.accountList.append(TA(id, email, password, name, address, phoneNum))
        User(id, email, password, name, address, phoneNum, role)
        User.save()

    def deleteAccount(self, accountIndex):
        User.objects.get(user_id=self.accountList.__getitem__(accountIndex)).delete()
        User.save()
        self.accountList.pop(accountIndex)

    def addCourse(self, courseid, coursename):
        # Precondition: Course parameters are valid
        # Postcondition: Course has been added to the courses list
        pass

    def deleteCourse(self,  courseIndex):
        pass



