from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("filter/new/", views.new_type, name="new_type"),
    path("filter/<t_filter>/", views.type_filter, name="type_filter"),
    path("today/", views.today_list, name="today_list"),
    path("new/", views.new_task, name="new_task"),
    path("completed/", views.completed, name="completed"),
    path("task/<int:id>/", views.task_detail, name="task_detail"),
    path("task/<int:id>/edit/", views.task_edit, name="task_edit"),
    path("task/<int:id>/done/", views.task_done, name="task_done"),
    path("task/<int:id>/delete/", views.task_delete, name="task_delete"),
]
