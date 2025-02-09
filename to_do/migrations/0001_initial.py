# Generated by Django 5.1.5 on 2025-01-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.CharField(max_length=511)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("deadline", models.DateField(blank=True, null=True)),
                ("is_done", models.BooleanField(default=False)),
                (
                    "tag",
                    models.ManyToManyField(
                        blank=True, related_name="tasks", to="to_do.tag"
                    ),
                ),
            ],
            options={
                "ordering": ("is_done",),
            },
        ),
    ]
