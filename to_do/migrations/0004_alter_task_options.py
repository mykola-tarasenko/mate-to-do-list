# Generated by Django 5.1.5 on 2025-01-31 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("to_do", "0003_remove_task_tag_task_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ("is_done", "-created_at")},
        ),
    ]
