from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from users.forms import LoginForm, UserRegForm
from django.contrib import messages


class UserLoginView(LoginView):
    form_class = LoginForm


class UserLogoutView(LogoutView):
    pass


def registration(request):
    form = UserRegForm()
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                message=f"Account has been successfully created",
            )
            return redirect("login")

    return render(request, "registration/signup.html", {"form": form})
