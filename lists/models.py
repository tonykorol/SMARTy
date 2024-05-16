from django.db import models
from django.conf import settings


class ListModel(models.Model):
    TYPES = [
        ("Home", "Home"),
        ("Work", "Work"),
        ("Education", "Education"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=50, verbose_name="List name")
    list_desc = models.TextField(verbose_name="List description", blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    list_type = models.CharField(max_length=10, choices=TYPES, default=TYPES[0][0])
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "lists"
        verbose_name = "User list"
        verbose_name_plural = "User lists"

    def __str__(self):
        return self.list_name
