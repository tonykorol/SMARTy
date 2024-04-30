from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from .forms import LoginForm


class UserLoginView(LoginView):
    form_class = LoginForm


class UserLogoutView(LogoutView):
    pass


def registration(request):
    return render(request, 'registration/signup.html')



