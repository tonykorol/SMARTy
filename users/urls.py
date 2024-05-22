from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView
from . import views

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("signup/", views.registration, name="signup"),
    path("account/", views.account, name="account"),
    path("account/edit", views.account_edit, name="account_edit"),
    path("account/change_password/", views.ChangePassword.as_view(), name="change_password"),
    path("account/password_change_done/", views.ChangePasswordDone.as_view(), name="password_change_done"),
]
