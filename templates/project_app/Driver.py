from templates.project_app.supervisor import Supervisor
from templates.project_app.instructor import Instructor
from templates.project_app.TA import TA
from templates.project_app.models import UserModel


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
        if(role == 0) :
            self.accountList[email] = (Supervisor(id, email, password, name, address, phoneNum))

        elif(role == 1) :
            self.accountList[email] = (Instructor(id, email, password, name, address, phoneNum))
        elif (role == 2):
            self.accountList[email] = (TA(id, email, password, name, address, phoneNum))

        added = UserModel(id, name, email, password,  address, phoneNum, role)
        added.save()

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



