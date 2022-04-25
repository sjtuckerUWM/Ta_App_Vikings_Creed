from TA import TA


class Section:
    # class variables
    TA = TA()
    courseNum = 0
    hasLab = False
    sectNum = 0
    meetingInfo = ""

    def __init__(self):
        pass

    def __init__(self, TA, hasLab):
        self.TA = TA
        self.hasLab = hasLab

    def __init__(self, TA, SectionNumber, MeetingTimePlace):
        self.TA = TA
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
    def getTA(self, TA):
        self.TA = TA

    def getCourseNum(self, courseNum):
        self.courseNum = courseNum

    def getLabStatus(self, labStatus):
        self.hasLab = labStatus

    def getSectionNum(self, sectionNum):
        self.sectNum = sectionNum

    def getMeetingPlace(self, meetingPlace):
        self.meetingInfo = meetingPlace
