from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.UserLogin.as_view(), name="logout"),
]
