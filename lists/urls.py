from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("filter/new/", views.new_type, name="new_type"),
    path("filter/<t_filter>/", views.type_filter, name="type_filter"),
    path("today/", views.today_list, name="today_list"),
    path("new/", views.new_list, name="new_list"),
    path("completed/", views.completed, name="completed"),
    path("list/<int:id>/", views.list_detail, name="list_detail"),
    path("list/<int:id>/edit/", views.list_edit, name="list_edit"),
    path("list/<int:id>/done/", views.task_done, name="task_done"),
    path("list/<int:id>/delete/", views.task_delete, name="task_delete"),
]
