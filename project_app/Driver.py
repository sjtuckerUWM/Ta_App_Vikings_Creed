from project_app.supervisor import Supervisor
from project_app.instructor import Instructor
from project_app.TA import TA
from project_app.course import Course
from project_app.section import Section
from project_app.models import UserModel, CourseModel, SectionModel

class Driver(object):
    def __init__(self):
        self.currentAccount = None
        self.accountList = []
        self.courseList = []
        self.fillAccounts()
        # to see if logIn works VVV
        self.addAccount(1, "email@a.com", "pass", "Test User", "USA", "123-456-7890", 0)

    def fillAccounts(self):

        things = UserModel
        for entry in things:
            if (entry.role == 0):
                self.accountList.append(Supervisor(entry.id, entry.email, entry.password, entry.name, entry.address, entry.phoneNum))

            elif (entry.role == 1):
                self.accountList.append(Instructor(entry.id, entry.email, entry.password, entry.name, entry.address, entry.phoneNum))
            elif (entry.role == 2):
                self.accountList.append(TA(entry.id, entry.email, entry.password, entry.name, entry.address, entry.phoneNum))

    def logIn(self, email, password):
        if UserModel.email.__contains__(email):
            if UserModel.objects.get(email=email).password is password:
                return 2
            return 1
        return 0

    def addAccount(self, id, email, password, name, address, phoneNum, role):
        if(role == 0) :
            self.accountList.append(Supervisor(id, email, password, name, address, phoneNum))

        elif(role == 1) :
            self.accountList.append(Instructor(id, email, password, name, address, phoneNum))
        elif (role == 2):
            self.accountList.append(TA(id, email, password, name, address, phoneNum))
        UserModel(id, email, password, name, address, phoneNum, role)
        UserModel.save()

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



