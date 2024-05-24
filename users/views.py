from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from lists.additions import get_types
from users.forms import LoginForm, UserRegForm, ChangePasswordForm, UserUpdForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib import messages
from django.utils.decorators import method_decorator


class UserLoginView(LoginView):
    form_class = LoginForm


class UserLogoutView(LogoutView):
    pass


class ChangePassword(PasswordChangeView):
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("password_change_done")
    form_class = ChangePasswordForm


class ChangePasswordDone(PasswordChangeDoneView):
    template_name = "registration/change_password_done.html"


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


@login_required
def account(request):
    user = request.user
    types = get_types(user)
    context = {"types": types}
    return render(request, "registration/account.html", context)


@login_required
def account_edit(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    form = UserUpdForm()
    if request.method == "POST":
        form = UserUpdForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data["email"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            upd_fields = []
            for key, value in form.cleaned_data.items():
                if form.cleaned_data[key]:
                    upd_fields.append(key)
                    user.key = form.cleaned_data[key]
            user.save(update_fields=upd_fields)
            return redirect("account")
    return render(request, "registration/account_edit.html", {"form": form})
