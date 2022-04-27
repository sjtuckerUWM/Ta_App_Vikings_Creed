from django.shortcuts import render, redirect
from django.views import View
from project_app.models import UserModel
from project_app.Driver import Driver


driver = Driver()


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "loginPage.html")

    def post(self, request):

        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        outcome = driver.logIn(email, password)

        if outcome == 0:
            return render(request, "loginPage.html", {"message": "email is not registered"})
        elif outcome == 1:
            return render(request, "loginPage.html", {"message": "bad password"})
        elif outcome == 2:

            request.session["currentUser"] = driver.getCurrentAccount().getEmail()
            return redirect('/home/')  # place url from url.py
        else:
            return render(request, "loginPage.html", {"message": "login error"})


class Home(View):
    def get(self, request):
        return render(request, "homePage.html")


class AccountManagement(View):
    def get(self, request):
        users = list(UserModel.objects.all())
        return render(request, "accountManagement.html", {"users": users})


class AddAccount(View):
    def get(self, request):
        return render(request, "addAccountPage.html")

    def post(self, request):
        driver = Driver(request.session["currentUser"])
        id = request.POST['id']
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        phoneNum = request.POST['phoneNum']
        role = request.POST['role']

        driver.addAccount(id, email, password, name, address, phoneNum, role)

        return redirect("/accounts")
