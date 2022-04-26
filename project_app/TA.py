from project_app.user import User


class TA(User):
    sectionList = []

    def __init__(self):
        pass

    def getSectionList(self):
        return self.sectionList

    def setSectionList(self, sectList):
        for i in sectList:
            self.sectionList.append(i)
