from django.db import models
from django.conf import settings


class TypeModel(models.Model):

    type_name = models.CharField(max_length=25, verbose_name="Type name", unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "types"
        verbose_name = "User type"
        verbose_name_plural = "User types"

    def __str__(self):
        return self.type_name


class TaskModel(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50, verbose_name="List name")
    task_desc = models.TextField(verbose_name="List description", blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    task_type = models.ForeignKey(TypeModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "lists"
        verbose_name = "User task"
        verbose_name_plural = "User tasks"

    def __str__(self):
        return self.task_name
