from django.shortcuts import render, redirect, reverse
from django.views.generic import View, CreateView
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import ProfileForm


class UserRegistration(CreateView):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user_role = user.profile.role
                messages.success(request, f"Hi {user.username} Login To your {user_role} Profile!")
                return redirect('login')

        context = {
            "form": form
        }
        return render(request, 'index.html', context)


class UserLogin(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("You are Logged In Now thats mean your Session is active")
            else:
                messages.error(request, "Username or Password is incorrect!")

        return render(request, 'login.html')












