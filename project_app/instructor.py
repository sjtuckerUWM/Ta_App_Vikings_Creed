from project_app.user import User


class Instructor(User):


    def __init__(self, id, email, password, name, address, phoneNum):
        User.__init__(self, id, email, password, name, address, phoneNum)
        self.courseList = []

    def getCourseList(self):
        return self.courseList

    def setCourseList(self, courseList):
        for i in courseList:
            self.courseList.append(i)
