from django.shortcuts import render, redirect
from django.views import View
from models import User


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "loginPage.html")

    def post(self, request):
        noSuchUser = False
        badPassword = False
        try:
            m = User.objects.get(name=request.POST['name'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:
            m = User(name=request.POST['name'], password=request.POST['password'])
            m.save()
            request.session["name"] = m.name
            return redirect("/things/")
        elif badPassword:
            return render(request, "home.html", {"message": "bad password"})
        else:
            request.session["name"] = m.name
            return redirect("/things/")
