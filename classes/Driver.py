from classes.course import Course
from classes.supervisor import Supervisor
from classes.instructor import Instructor
from classes.TA import TA
from proj_app.models import MyUserModel, CourseModel
import re

# Driver is the class that helps us perform the required actions with the current user
class Driver(object):

    # constructor
    def __init__(self, currentAccount=None):
        self.currentAccount = currentAccount
        self.accountList = {}
        self.courseList = {}
        # self.addAccount(1, "email@a.com", "pass", "Test User", "USA", "123-456-7890", 0)
        c = CourseModel(course_id=5,dept_code="BIO SCI", name="coursename")
        self.fillAccounts()
        self.fillCourses()
        # to see if logIn works VVV
        # self.addAccount(1, "email@a.com", "pass", "Test User", "USA", "123-456-7890", 0)

    def getCurrentAccount(self):
        return self.currentAccount

    def fillCourses(self):
        things = list(CourseModel.objects.all())
        # filling the courses with entered values
        for entry in things:
            print(entry.name)
            self.courseList[entry.course_id] = Course(entry.course_id, entry.name)
            if(entry.assigned_instructor is not None):
                self.courseList[entry.course_id].assignInstructor(entry.assigned_instructor)
            if (entry.assigned_tas is not None):
                self.courseList[entry.course_id].assignTA(list(entry.assigned_tas.all()))

    def fillAccounts(self):
        # things = UserModel.objects.iterator(100
        things = list(MyUserModel.objects.all())
        # filling the accounts with entered values
        for entry in things:
            print(entry.email)
            # Supervisor
            if (entry.role == 0):
                self.accountList[entry.email] = (Supervisor(entry.user_id, entry.email, entry.password, entry.name, entry.address, entry.phone_number))
            # Instructor
            elif (entry.role == 1):
                self.accountList[entry.email] = (Instructor(entry.user_id, entry.email, entry.password, entry.name, entry.address, entry.phone_number))
            # TA
            elif (entry.role == 2):
                self.accountList[entry.email] = (TA(entry.user_id, entry.email, entry.password, entry.name, entry.address, entry.phone_number))

    def logIn(self, email, password):
        # if self.currentAccount != None: return RuntimeError
        try:
            m = MyUserModel.objects.get(email=email)
            if MyUserModel.objects.get(email=email).password == password:
                self.currentAccount = self.accountList[email]
                # if both email and password are correct
                return 2
            # if one of them fails
            return 1
        except:
            # If both of them fails
            return 0


    def addAccount(self, id, email, password, name, address, phoneNum, role):
        a = ["","","","","","",""]
        # checking if the id is between 0 and 999
        if (re.findall("[1-9][0-9]*", id) != [id]) or int(id)>9999 : a[0] = "Invalid, integer between 0 and 9999"
        else:
            try:
                m = MyUserModel.objects.get(user_id=id)
                a[0] = "Invalid, ID already in use by " + m.email
            except:
                pass
        # or checking if id is in use by another user
        if (re.findall("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) != [email]) or (len(str(email))>99): a[1] =  "Invalid"
        else:
            try:
                m = MyUserModel.objects.get(email=email)
                a[1] = "Invalid, Email already in use by " + m.name
            except:
                pass

        # checking if password is valid
        if (len(str(password))<8) or (len(str(password))>19): a[2] =  "Invalid, 8 or more characters"
        if (re.search("\d", name) != None) or (len(str(name))>49) or (len(str(name))<1): a[3] =  "Invalid, can't contain digits"
        if (len(str(address))<3) or (len(str(address))>99): a[4] =  "Invalid, length should be >= 3 and < 100"

        # checking if phoneNum is correct form
        if (re.findall("[0-9]{3}\-[0-9]{3}\-[0-9]{4}|[0-9]{10}", phoneNum) != [phoneNum]): a[5] =  "Invalid, Format should be: \"123-456-7890\" OR \"1234567890\""
        if a != ["","","","","","",""]:
            return a

        # checking the roles
        if(role == 0) :
            self.accountList[email] = (Supervisor(id, email, password, name, address, phoneNum))

        elif(role == 1) :
            self.accountList[email] = (Instructor(id, email, password, name, address, phoneNum))
        elif (role == 2):
            self.accountList[email] = (TA(id, email, password, name, address, phoneNum))

        added = MyUserModel(id, name, email, password, address, phoneNum, role)
        added.save()
        return a

    def deleteAccount(self, ID):
        MyUserModel.objects.get(user_id=ID).delete()


    def editAccount(self, oldID, id, email, password, name, address, phoneNum, role):
        a = ["", "", "", "", "", "", ""]
        # checking if the id is between 0 and 999
        if (re.findall("[1-9][0-9]*", id) != [id]) or int(id) > 9999:
            a[0] = "Invalid, integer between 0 and 9999"
        # or checking if id is in use by another user
        elif(int(id)!=oldID):
            try:
                m = MyUserModel.objects.get(user_id=id)
                a[0] = "Invalid, ID already in use by " + m.email
            except:
                pass

        if (re.findall("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) != [email]) or (len(str(email)) > 99):
            a[1] = "Invalid"
        elif(MyUserModel.objects.get(user_id=oldID).email != email):
            try:
                m = MyUserModel.objects.get(email=email)
                a[1] = "Invalid, Email already in use by " + m.name
            except:
                pass
        # checking if password is valid
        if (len(str(password)) < 8) or (len(str(password)) > 19): a[2] = "Invalid, 8 or more characters"
        if (re.search("\d", name) != None) or (len(str(name)) > 49) or (len(str(name)) < 1): a[
            3] = "Invalid, can't contain digits"
        if (len(str(address)) < 3) or (len(str(address)) > 99): a[4] = "Invalid, length should be >= 3 and < 100"

        # checking if phoneNum is correct form
        if (re.findall("[0-9]{3}\-[0-9]{3}\-[0-9]{4}|[0-9]{10}", phoneNum) != [phoneNum]): a[
            5] = "Invalid, Format should be: \"123-456-7890\" OR \"1234567890\""
        if a != ["", "", "", "", "", "", ""]:
            return a
        self.deleteAccount(oldID)
        # checking the roles
        if (role == 0):
            self.accountList[email] = (Supervisor(id, email, password, name, address, phoneNum))

        elif (role == 1):
            self.accountList[email] = (Instructor(id, email, password, name, address, phoneNum))
        elif (role == 2):
            self.accountList[email] = (TA(id, email, password, name, address, phoneNum))

        added = MyUserModel(id, name, email, password, address, phoneNum, role)
        added.save()
        return a

    def addCourse(self, courseid, coursedep, coursename):
        # Precondition: Course parameters are valid
        # Postcondition: Course has been added to the courses list
        a = ["", "", ""]
        # checking if the course id is between 0 and 999
        if (re.findall("[1-9][0-9]*", courseid) != [courseid]) or int(courseid) > 9999:
            a[0] = "Invalid, integer between 0 and 9999"
        else:
            try:
                m = CourseModel.objects.get(course_id=courseid)
                a[0] = "Invalid, ID already in use by " + m.name
            except:
                pass
        # checking if the coursedep is valid
        if (coursedep == ""):
            a[1] = "Invalid, Select a department"
        # checking the coursename characters numbers are between 5 and 19
        if (len(str(coursename)) < 5) or (len(str(coursename)) > 19):
            a[2] = "Invalid, 5 or more characters"
        if a != ["", "", ""]:
            return a

        self.courseList[courseid] = (Course(courseid, coursedep, coursename))

        # Finally, creating the course object accoording to Coursemodel
        added = CourseModel(course_id=courseid,dept_code=coursedep, name=coursename)
        added.save()
        return a

    def deleteCourse(self,  ID):
        CourseModel.objects.get(course_id=ID).delete()

    def assignToCourse(self, course_id, instructor_id, ta_ids):
        #assigning Instructors and TAs to courses
        course = CourseModel.objects.get(course_id=course_id)
        course.assigned_instructor = instructor_id
        for i in ta_ids:
            course.assigned_tas.add(i)
        course.save()






