from classes.section import Section


class Course:

    def __init__(self, courseID=1, courseDep="COMP SCI", CourseName="Intro to CS"):
        self.courseID = courseID
        self.courseDep = courseDep
        self.courseName = CourseName
        self.TA_list = []

    def assignTA(self, TA_list):
        self.setTA_list(TA_list)

    def assignInstructor(self, instructorId):
        self.setInstructor(instructorId)

    def AddSection(self, CourseNum, TA, SectionNumber, MeetingTimePlace):
        # id, email, password, name, address, phoneNum
        if self.courseID == CourseNum:
            s = Section(TA, SectionNumber, MeetingTimePlace)
            self.sectionList.append(s)
            return True

        return False

    def DeleteSection(self, SectionID):
        for i in self.sectionList:
            if i.sectNum == SectionID:
                self.sectionList.remove(i)
                return True

        # if the id wasn't in the list
        return False

    def containsTA(self, TA):
        for i in self.TA_list:
            if i == TA:
                return True
        return False

    # Getters
    def getCourseID(self):
        return self.courseID

    def getCourseName(self):
        return self.courseName

    def getInstructor(self):
        return self.instructorId

    def getSectionList(self):
        return self.SectionList

    def getTA_list(self):
        return self.TA_list

    # Setters
    def setCourseID(self, courseId):
        self.courseID = courseId

    def setCourseName(self, courseName):
        self.courseName = courseName

    def setInstructor(self, instructorID):
        self.instructorId = instructorID

    def setSectionList(self, sectionList):
        for i in sectionList:
            self.sectionList.append(i)

    def setTA_list(self, TA_list):
        for i in TA_list:
            self.TA_list.append(i)
