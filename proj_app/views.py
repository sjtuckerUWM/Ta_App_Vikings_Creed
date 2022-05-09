from django.shortcuts import render, redirect
from django.views import View

from proj_app.models import MyUserModel, CourseModel, Department
from classes.Driver import Driver



# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "mainTemplates/loginPage.html")

    def post(self, request):
        driver = Driver()
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        outcome = driver.logIn(email, password)

        if outcome == 0:
            return render(request, "mainTemplates/loginPage.html", {"message": "email is not registered"})
        elif outcome == 1:
            return render(request, "mainTemplates/loginPage.html", {"message": "bad password"})
        elif outcome == 2:

            request.session["currentUser"] = driver.getCurrentAccount().getEmail()
            return redirect('/home/')  # place url from url.py
        else:
            return render(request, "mainTemplates/loginPage.html", {"message": "login error"})


class Home(View):
    def get(self, request):
        role_id = MyUserModel.objects.get(email=request.session["currentUser"]).role
        return render(request, "mainTemplates/homePage.html", {"role_id": role_id})


class AccountManagement(View):
    def get(self, request):
        users = list(MyUserModel.objects.all())
        return render(request, "mainTemplates/accountManagement.html", {"users": users})


class AddAccount(View):
    def get(self, request):
        return render(request, "mainTemplates/addAccountPage.html")

    def post(self, request):
        driver = Driver(request.session["currentUser"])
        id = request.POST['id']
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        phoneNum = request.POST['phoneNum']
        role = request.POST['role']
        message = 'Blank parameter or paramaters'

        if id == '' or email == '' or password == '' or name == '' or address == '' or phoneNum == '' or role == '':
            return render(request, "mainTemplates/addAccountPage.html", {'message': message})

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
            'v_id': verify[0],
            'v_email': verify[1],
            'v_password': verify[2],
            'v_name': verify[3],
            'v_address': verify[4],
            'v_phoneNum': verify[5],
        }
        return render(request, "mainTemplates/addAccountPage.html", values)



class DeleteAccount(View):
    def get(self, request, id):
        print(str(id))
        return render(request, "mainTemplates/deleteAccountPage.html")

    def post(self, request, id):
        driver = Driver(request.session["currentUser"])
        driver.deleteAccount(id)
        return redirect("/accounts")

class EditAccount(View):
    def get(self, request, id):
        print(str(id))
        driver = Driver(request.session["currentUser"])
        account = driver.accountList[MyUserModel.objects.get(user_id=id).email]
        verify = ["", "", "", "", "", "", ""]
        roleStr = ""
        role = MyUserModel.objects.get(user_id=id).role
        request.session['editRole'] = role

        if(role == 0):
            roleStr = "Supervisor"
        elif(role == 1):
            roleStr = "Instructor"
        elif(role == 2):
            roleStr = "TA"
        request.session['editRoleString'] = roleStr
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
            return redirect("/accounts")

        roleStr = request.session['editRoleString']


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

class ManageCourse(View):
    def get(self, request):
        courses = list(CourseModel.objects.all())
        return render(request, "mainTemplates/courseManagement.html", {"courses": courses})
class AddCourse(View):
    def get(self, request):
        return render(request, "mainTemplates/addCoursePage.html", {"departments": Department.choices})

    def post(self, request):
        print(Department('COMP SCI').name)
        # print(Department['Comp Sci'])
        driver = Driver(request.session["currentUser"])
        id = request.POST['id']
        dep = request.POST['dep']
        print("dep is " + dep)
        name = request.POST['name']
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
        return render(request, "mainTemplates/assignToCoursePage.html")