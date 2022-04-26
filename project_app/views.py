from django.shortcuts import render, redirect
from django.views import View

from project_app.models import UserModel
from project_app.Driver import Driver

# driver = Driver() testing session based driver



# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "loginPage.html")

    def post(self, request):

        driver = Driver()
        email = request.POST['email']
        password = request.POST['password']
        outcome = driver.logIn(email, password)

        if outcome == 0:
            return render(request, "loginPage.html", {"message": "email is not registered"})
        elif outcome == 1:
            return render(request, "loginPage.html", {"message": "bad password"})
        elif outcome == 2:
            request.session["driver"] = driver
            return redirect("homePage.html")  # place url from url.py
        else:
            return render(request, "loginPage.html", {"message": "login error"})

