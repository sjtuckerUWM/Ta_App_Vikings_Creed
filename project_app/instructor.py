from project_app.user import User


class Instructor(User):
    courseList = []

    def __init__(self):
        pass

    def getCourseList(self):
        return self.courseList

    def setCourseList(self, courseList):
        for i in courseList:
            self.courseList.append(i)
