from templates.project_app.user import User


class TA(User):


    def __init__(self, id, email, password, name, address, phoneNum):
        User.__init__(self, id, email, password, name, address, phoneNum)
        self.sectionList = []

    def getSectionList(self):
        return self.sectionList

    def setSectionList(self, sectList):
        for i in sectList:
            self.sectionList.append(i)
