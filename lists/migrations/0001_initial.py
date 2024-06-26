# Generated by Django 5.0.4 on 2024-05-23 15:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TypeModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type_name",
                    models.CharField(
                        max_length=25, unique=True, verbose_name="Type name"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User type",
                "verbose_name_plural": "User types",
                "db_table": "types",
            },
        ),
        migrations.CreateModel(
            name="TaskModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "task_name",
                    models.CharField(max_length=50, verbose_name="List name"),
                ),
                (
                    "task_desc",
                    models.TextField(blank=True, verbose_name="List description"),
                ),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("start_time", models.TimeField(blank=True, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "task_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lists.typemodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "User task",
                "verbose_name_plural": "User tasks",
                "db_table": "lists",
            },
        ),
    ]
