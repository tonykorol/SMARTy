from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control col-12",
                "placeholder": "Enter your login",
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control col-12",
                "placeholder": "Enter your password",
            }
        ),
    )


class UserRegForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control col-12", "placeholder": "Enter password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control col-12", "placeholder": "Repeat password"}
        )
    )

    class Meta:
        model = User
        fields = ("username", "email")
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control col-12",
                    "placeholder": "Enter username",
                    "autofocus": True,
                }
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control col-12", "placeholder": "Enter email"}
            ),
        }

    def clean_password2(self):
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data["password2"]


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter old password",
                "autofocus": True,
            }
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter new password",
            }
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Repeat new password",
            }
        )
    )


class UserUpdForm(forms.ModelForm):
    username_validator = UnicodeUsernameValidator()

    username = forms.CharField(
        validators=[username_validator],
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control col-12",
                "placeholder": "Enter a new Username or leave blank",
            },

        ),
    )

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control col-12",
                    "placeholder": "Enter a new Email or leave blank",
                }
            ),
            "first_name": forms.EmailInput(
                attrs={
                    "class": "form-control col-12",
                    "placeholder": "Enter a new First Name or leave blank",
                }
            ),
            "last_name": forms.EmailInput(
                attrs={
                    "class": "form-control col-12",
                    "placeholder": "Enter a new Last Name or leave blank",
                }
            ),
        }
