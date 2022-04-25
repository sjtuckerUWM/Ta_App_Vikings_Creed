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
        pass

    def addAccount_(self, id, email, password, name, address, phoneNum, role):
        if(role is 0) :
            self.accountList.append(Supervisor(id, email, password, name, address, phoneNum))
        elif(role is 1) :
            self.accountList.append(Instructor(id, email, password, name, address, phoneNum))
        elif (role is 2):
            self.accountList.append(TA(id, email, password, name, address, phoneNum))



    def deleteAccount_(self, accountIndex):
        self.accountList.pop(accountIndex)

    def addCourse_(self, courseid, coursename):
        # Precondition: Course parameters are valid
        # Postcondition: Course has been added to the courses list
        pass

    def deleteCourse_(self,  courseId):
    # Precondition: The course ID being passed in is of the correct data type
    #Postcondition: Deletes course with matching ID from the database
        pass



