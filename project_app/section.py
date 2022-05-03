from project_app.TA import TA


class Section:
    # class variables
    TA = None  # TA("1", "TA@test.com", "pass1234", "Test TA", "USA", "123-456-7890")
    courseNum = 0
    hasLab = False
    sectNum = 0
    meetingInfo = ""

    def __init__(self):
        pass

    def __init__(self, ta, hasLab):
        self.TA = ta
        self.hasLab = hasLab

    def __init__(self, ta, SectionNumber, MeetingTimePlace):
        self.TA = ta
        self.sectNum = SectionNumber
        self.meetingInfo = MeetingTimePlace

    # Getters
    def getTA(self):
        return self.TA

    def getCourseNum(self):
        return self.courseNum

    def getLabStatus(self):
        return self.hasLab

    def getSectionNum(self):
        return self.sectNum

    def getMeetingPlace(self):
        return self.meetingInfo

    # Setters
    def getTA(self, ta):
        self.TA = ta

    def getCourseNum(self, courseNum):
        self.courseNum = courseNum

    def getLabStatus(self, labStatus):
        self.hasLab = labStatus

    def getSectionNum(self, sectionNum):
        self.sectNum = sectionNum

    def getMeetingPlace(self, meetingPlace):
        self.meetingInfo = meetingPlace
