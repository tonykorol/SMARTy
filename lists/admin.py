from django.contrib import admin
from lists.models import TaskModel, TypeModel


admin.site.register(TaskModel)
admin.site.register(TypeModel)
