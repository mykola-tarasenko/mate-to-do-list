from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=511)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, blank=True, related_name="tasks")

    class Meta:
        ordering = ("is_done", )