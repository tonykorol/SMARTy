from django.contrib.auth.views import LoginView
from .forms import LoginForm


class UserLogin(LoginView):
    form_class = LoginForm
