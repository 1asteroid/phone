from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "user_auth_templates/login.html", context=context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }

        login_form = AuthenticationForm(data=data)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')

        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, 'user_auth_templates/login.html', context)


class UserRegisterView(View):
    def get(self, request):
        return render(request, "user_auth_templates/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password_1"]
        password2 = request.POST["password_2"]

        if password1 == password2:
            user_check = User.objects.filter(username=username)
            if user_check:
                return render(request, 'user_auth_templates/register.html')
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password1)
                user.save()
                return redirect('home')

        else:
            return render(request, 'user_auth_templates/register.html')


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
