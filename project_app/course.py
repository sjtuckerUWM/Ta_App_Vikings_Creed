class Course:
    # Class Variables
    courseID = 0
    courseName = ""
    instructorId = 0
    sectionList = []
    TA_list = []

    # Constructors
    def __init__(self):
        pass

    def __init__(self, courseID, CourseName):
        self.courseID = courseID
        self.courseName = CourseName

    def assignTA(self, TA_list):
        self.setTA_list(TA_list)

    def assignInstructor(self, instructorId):
        self.setInstructor(instructorId)

    def AddSection(self, CourseNum, TA, SectionNumber, MeetingTimePlace):
        # TODO
        pass

    def DeleteSection(self, SectionID):
        pass

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

    def setSectionList(self, *sectionList):
        for i in sectionList:
            self.sectionList.append(i)

    def setTA_list(self, *TA_list):
        for i in TA_list:
            self.TA_list.append(i)
