from django.shortcuts import render, redirect
from django.views import View

from proj_app.models import MyUserModel, CourseModel, Department, SectionModel
from classes.Driver import Driver



# view for Login
class Login(View):
    # get method to render HTML page of Login
    def get(self, request):
        try:
            del request.session['currentUser']
        except KeyError:
            pass
        try:
            del request.session['currentRole']
        except KeyError:
            pass
        return render(request, "mainTemplates/loginPage.html")


    def post(self, request):
        driver = Driver()
        email = request.POST['email']  # posting the email
        password = request.POST['password']   # posting the password
        print(email)
        print(password)
        outcome = driver.logIn(email, password)  # getting the outcome

        if outcome == 0:   # if email is bad
            return render(request, "mainTemplates/loginPage.html", {"message": "email is not registered"})
        elif outcome == 1:  # if password bad
            return render(request, "mainTemplates/loginPage.html", {"message": "bad password"})
        elif outcome == 2:  # if both correct

            request.session["currentUser"] = driver.getCurrentAccount().getEmail()
            request.session["currentRole"] = MyUserModel.objects.get(email=request.session["currentUser"]).role
            return redirect('/home/')  # place url from url.py
        else:
            return render(request, "mainTemplates/loginPage.html", {"message": "login error"})

# view for home page
class Home(View):
    def get(self, request):
        try:
            role_id = request.session["currentRole"]
        except KeyError:
            return redirect('/')
        return render(request, "mainTemplates/homePage.html", {"role_id": role_id})

# view for Account management
class AccountManagement(View):
    def get(self, request):
        try:
            role_id = request.session["currentRole"]
            if role_id != 0:
                return redirect('/home/')
        except KeyError:
            return redirect('/')
        users = list(MyUserModel.objects.all())  # getting all the users
        return render(request, "mainTemplates/accountManagement.html", {"users": users})

#  view for Add account
class AddAccount(View):
    def get(self, request):
        try:
            role_id = request.session["currentRole"]
            if role_id != 0:
                return redirect('/home/')
        except KeyError:
            return redirect('/')
        return render(request, "mainTemplates/addAccountPage.html")

    def post(self, request):
        driver = Driver(request.session["currentUser"])  # getting the current user in Driver
        # posting the parameters
        id = request.POST['id']
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        phoneNum = request.POST['phoneNum']
        role = int(request.POST['role'])
        print(role)
        print(role is int)


        # verifying parameters are not blank and making sure parameters aligned correctly
        verify = driver.addAccount(id, email, password, name, address, phoneNum, role)
        if verify == ["","","","","","",""]:
            return redirect("/accounts")
        values = {
            'id': request.POST['id'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'name': request.POST['name'],
            'address': request.POST['address'],
            'phoneNum': request.POST['phoneNum'],
            'role': request.POST['role'],
            'v_id': verify[0],
            'v_email': verify[1],
            'v_password': verify[2],
            'v_name': verify[3],
            'v_address': verify[4],
            'v_phoneNum': verify[5],
            'v_role': verify[6],
        }
        return render(request, "mainTemplates/addAccountPage.html", values)


# view for delete page
class DeleteAccount(View):
    def get(self, request, id):
        #print(str(id))
        try:
            role_id = request.session["currentRole"]
            if role_id != 0:
                return redirect('/home/')
        except KeyError:
            return redirect('/')
        return render(request, "mainTemplates/deleteAccountPage.html")

    def post(self, request, id):
        driver = Driver(request.session["currentUser"])  # getting the current user
        driver.deleteAccount(id)  # deleting
        return redirect("/accounts")

# view for Edit account
class EditAccount(View):
    def get(self, request, id):
        #print(str(id))
        try:
            role_id = request.session["currentRole"]
            if role_id != 0:
                return redirect('/home/')
        except KeyError:
            return redirect('/')

        driver = Driver(request.session["currentUser"])
        account = driver.accountList[MyUserModel.objects.get(user_id=id).email]  # getting the account by user id
        verify = ["", "", "", "", "", "", ""]
        roleStr = ""
        role = MyUserModel.objects.get(user_id=id).role  # getting the role
        request.session['editRole'] = role

        # checking the roles
        if(role == 0):
            roleStr = "Supervisor"
        elif(role == 1):
            roleStr = "Instructor"
        elif(role == 2):
            roleStr = "TA"
        request.session['editRoleString'] = roleStr   # putting blank role

        # verifying all parameters aligned correctly
        values = {
            'id': account.getID(),
            'email': account.getEmail(),
            'password': account.getPassword(),
            'name': account.getName(),
            'address': account.getAddress(),
            'phoneNum': account.getPhoneNum(),
            'role': roleStr,
            'v_id': verify[0],
            'v_email': verify[1],
            'v_password': verify[2],
            'v_name': verify[3],
            'v_address': verify[4],
            'v_phoneNum': verify[5],
        }
        return render(request, "mainTemplates/editAccountPage.html", values)

    def post(self, request, id):
        oldID = id
        # getting the current user and posting the parameters
        driver = Driver(request.session["currentUser"])
        inputID = request.POST['id']
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        phoneNum = request.POST['phoneNum']
        role = request.session['editRole']
        verify = driver.editAccount(oldID, inputID, email, password, name, address, phoneNum, role)
        if verify == ["", "", "", "", "", "", ""]:
            return redirect("/accounts")   # returning the accounts if parameters are blank

        roleStr = request.session['editRoleString']

        # verifying all parameters aligned correctly
        values = {
            'id': request.POST['id'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'name': request.POST['name'],
            'address': request.POST['address'],
            'phoneNum': request.POST['phoneNum'],
            'role': roleStr,
            'v_id': verify[0],
            'v_email': verify[1],
            'v_password': verify[2],
            'v_name': verify[3],
            'v_address': verify[4],
            'v_phoneNum': verify[5],
        }
        return render(request, "mainTemplates/editAccountPage.html", values)

# view for Manage Course page
class ManageCourse(View):
    def get(self, request):
        try:
            role_id = request.session["currentRole"]
            if role_id != 0 & role_id != 1:
                return redirect('/home/')
        except KeyError:
            return redirect('/')

        courses = list(CourseModel.objects.all())  # getting all the courses
        user = MyUserModel.objects.get(email=request.session["currentUser"])
        missingPeople = False

        # checks if there are no tas and no instructors
        if (list(MyUserModel.objects.filter(role=1)) == [] or list(MyUserModel.objects.filter(role=2)) == []):
            missingPeople = True



        return render(request, "mainTemplates/courseManagement.html", {"courses": courses, 'user': user, 'missingPeople': missingPeople})

# view for Add course page
class AddCourse(View):
    def get(self, request):
        try:
            role_id = request.session["currentRole"]
            if role_id != 0 & role_id != 1:
                return redirect('/home/')
        except KeyError:
            return redirect('/')
        return render(request, "mainTemplates/addCoursePage.html", {"departments": Department.choices})

    def post(self, request):
        print(Department('COMP SCI').name)  # printing department name
        # print(Department['Comp Sci'])
        driver = Driver(request.session["currentUser"])
        id = request.POST['id']
        dep = request.POST['dep']
        print("dep is " + dep)
        name = request.POST['name']

        # verifying page goes back to courses page if parameters are blank, and check to see parameters aligned correctly
        verify = driver.addCourse(id, dep, name)
        if verify == ["", "", ""]:
            return redirect("/courses")
        values = {
            'id': request.POST['id'],
            'name': request.POST['name'],
            'dep': request.POST['dep'],
            'v_id': verify[0],
            'v_dep': verify[1],
            'v_name': verify[2],
            "departments": Department.choices
        }
        return render(request, "mainTemplates/addCoursePage.html", values)


class AssignToCourse(View):
    def get(self, request, id):
        try:
            role_id = request.session["currentRole"]
            if role_id != 0 & role_id != 1:
                return redirect('/home/')
        except KeyError:
            return redirect('/')
        curCourse = CourseModel.objects.get(course_id=id)
        user = MyUserModel.objects.get(email=request.session["currentUser"])
        values = {
            'course': curCourse,
            'instructorList': list(MyUserModel.objects.filter(role=1).all()),
            'taList': list(MyUserModel.objects.filter(role=2).all()),
            'user': user,
        }
        print(curCourse.assigned_instructor)
        if (len(values['instructorList']) < 1) :
            return render(request, "mainTemplates/assignToCoursePage.html",{'error': 'There is no instructor to assign'})
        if (len(values['taList']) < 1) :
            return render(request, "mainTemplates/assignToCoursePage.html",{'error': 'There is no TA to assign'})

        if (curCourse.assigned_instructor is not None):
            values['instructor'] = curCourse.assigned_instructor
        if (curCourse.assigned_tas is not None ):
            values['tas'] = list(curCourse.assigned_tas.all())
        return render(request, "mainTemplates/assignToCoursePage.html", values)
    def post(self, request, id):

        driver = Driver(request.session["currentUser"])
        curCourse = CourseModel.objects.get(course_id=id)
        print(request.POST.getlist('taIDs'))
        values = {
            'course': curCourse,
            'instructorList': list(MyUserModel.objects.filter(role=1).all()),
            'taList': list(MyUserModel.objects.filter(role=2).all()),
        }
        print(request.POST['instructor'])
        if(request.POST['instructor']!=''):
            instruct = MyUserModel.objects.get(user_id=request.POST['instructor'])
            values['instructor'] = instruct
            curCourse.assigned_instructor = instruct

        curCourse.assigned_tas.clear()

        if (request.POST.getlist('taIDs') != []):
            taIDs = request.POST.getlist('taIDs')
            tas = []
            for i in taIDs:
                cur = MyUserModel.objects.get(user_id=int(i))
                tas.append(cur)
                curCourse.assigned_tas.add(cur)
            values['tas'] = tas
        curCourse.save()

        return render(request, "mainTemplates/assignToCoursePage.html", values)
class ManageSections(View):
    def get(self, request, id):
        try:
            role_id = request.session["currentRole"]
            if role_id != 0 & role_id != 1:
                return redirect('/home/')
        except KeyError:
            return redirect('/')
        curCourse = CourseModel.objects.get(course_id=id)
        values = {
            'course': curCourse,
            'taList': list(curCourse.assigned_tas.all()),
            'sectionList': list(SectionModel.objects.filter(course=curCourse).all())
            # section model has a course field, but course doesn't have a sections field
        }
        return render(request, "mainTemplates/sectionManagement.html", values)

    def post(self, request, id):
        driver = Driver(request.session["currentUser"])
        curCourse = CourseModel.objects.get(course_id=id)
        sectionList = list(SectionModel.objects.filter(course=curCourse).all())
        for i in sectionList:
            taID = request.POST[("TA/" + str(i.section_id))]
            if(taID!=''):
                i.assigned_ta = MyUserModel.objects.get(user_id=taID)
            else:
                i.assigned_ta = None
            i.save()

        # prob not needed
        sectionList = list(SectionModel.objects.filter(course=curCourse).all())

        values = {
            'course': curCourse,
            'taList': list(curCourse.assigned_tas.all()),
            'sectionList': sectionList
            # section model has a course field, but course doesn't have a sections field
        }
        return render(request, "mainTemplates/sectionManagement.html", values)


class AddSection(View):
    def get(self, request, id):
        try:
            role_id = request.session["currentRole"]
            if role_id != 0 & role_id != 1:
                return redirect('/home/')
        except KeyError:
            return redirect('/')
        curCourse = CourseModel.objects.get(course_id=id)
        values = {
            'course': curCourse,
            'taList': list(curCourse.assigned_tas.all()),
        }
        return render(request, "mainTemplates/addSectionPage.html", values)

    def post(self, request, id):
        curCourse = CourseModel.objects.get(course_id=id)
        sectionNumber = request.POST['SectionNumber']
        ta = request.POST['TA']
        if sectionNumber != '':
            newSection = SectionModel(name=sectionNumber, course=curCourse)
            if ta != "":
                newSection.assigned_ta = MyUserModel.objects.get(user_id=int(ta))
            newSection.save()
            return redirect("/sections/" + str(id) + "/" )



        values = {
            'course': curCourse,
            'v_num': 'Enter A Section Number!',
            'taList': list(curCourse.assigned_tas.all()),
            # section model has a course field, but course doesn't have a sections field
        }
        return render(request, "mainTemplates/addSectionPage.html", values)

class Contact(View):
    def get(self, request):
        try:
            request.session["currentRole"]
        except KeyError:
            return redirect('/')
        supervisors = list(MyUserModel.objects.filter(role=0).all())  # getting all the users
        instructors = list(MyUserModel.objects.filter(role=1).all())
        TAs = list(MyUserModel.objects.filter(role=2).all())
        values = {
            "supervisors": supervisors,
            "instructors": instructors,
            "TAs": TAs
        }
        return render(request, "mainTemplates/contactsPage.html", values)

