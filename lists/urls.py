from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("today/", views.today_list, name="today_list"),
    path("new/", views.new_list, name="new_list"),
    path("list/<int:id>/", views.list_detail, name="list_detail"),
    path("list/<int:id>/edit/", views.list_edit, name="list_edit"),
    path("list/<int:id>/done/", views.task_done, name="task_done"),
    path("list/<int:id>/delete/", views.task_delete, name="task_delete"),
]
