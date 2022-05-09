from classes.user import User


class Instructor(User):

    #constructor
    def __init__(self, id, email, password, name, address, phoneNum):
        # Precondition: All fields passed in are valid datatypes
        # Postcondition: An user is created with the specified information stored in their account

        User.__init__(self, id, email, password, name, address, phoneNum)
        self.courseList = []

    # getter
    def getCourseList(self):
        return self.courseList

    # setter
    def setCourseList(self, courseList):
        for i in courseList:
            self.courseList.append(i)
