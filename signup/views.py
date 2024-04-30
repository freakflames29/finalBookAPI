from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from .form import SignupForm, LoginForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required


class Signup(View):

    def get(self, rq):
        form = SignupForm(rq)

        form = SignupForm()
        return render(rq, "signup/signup.html", {
            "form": form
        })

    def post(self, rq):
        form = SignupForm(rq.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            c_password = form.cleaned_data['c_password']
            print("*" * 100)
            print(username)
            print("*" * 100)

            lowerpass = password.lower()
            confirm_lowerpass = c_password.lower()

            print("*" * 100)
            print(f"{lowerpass} == {confirm_lowerpass}")
            print("*" * 100)

            username_check = User.objects.filter(username=username)
            if len(username_check) > 0:
                messages.error(rq, "User already exists")
                return render(rq, "signup/signup.html", {
                    "form": form
                })
            elif lowerpass != confirm_lowerpass:
                messages.error(rq, "Password and password confirmation is not matching")
                return render(rq, "signup/signup.html", {
                    "form": form
                })
            else:
                user = User.objects.create(
                    username=username,
                    email=email
                )
                user.set_password(password)
                user.save()
                messages.success(rq, "registration is successfull login to continue")

                return redirect("loginpath")



def loginView(rq):
    if rq.method == "GET":
        form = LoginForm()
        return render(rq, "signup/login.html", {
            "form": form
        })
    elif rq.method == "POST":
        form = LoginForm(rq.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                messages.success(rq, "Login succesfully")
                print("$" * 100)
                print("before token")
                print(user)
                print("$" * 100)
                token = Token.objects.get_or_create(user=user)
                login(rq, user)
                print("$" * 100)
                print("after token")
                print(user)
                print("$" * 100)

                return redirect("tokenpath")
            else:
                messages.error(rq, "username/password is incorrect")
                return render(rq, "signup/login.html", {
                    "form": form
                })


def logoutView(rq):
    logout(rq)
    messages.success(rq, "you are loggecd out")
    return redirect("loginpath")


@login_required(login_url='loginpath')
def tokenView(rq):
    user = rq.user
    print("*" * 100)
    print(f" THE LOGGED IN USER is = {user}")
    print("*" * 100)
    token = Token.objects.get(user=user)
    return render(rq, "signup/Token.html", {
        "token": token
    })
