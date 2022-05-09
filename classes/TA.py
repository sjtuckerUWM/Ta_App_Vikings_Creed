from classes.user import User


class TA(User):

    # constructor
    def __init__(self, id, email, password, name, address, phoneNum):
        User.__init__(self, id, email, password, name, address, phoneNum)
        self.sectionList = []

    # getter
    def getSectionList(self):
        return self.sectionList

    # setter
    def setSectionList(self, sectList):
        for i in sectList:
            self.sectionList.append(i)
