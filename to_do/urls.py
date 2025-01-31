from django.contrib import admin
from django.urls import path, include

from to_do.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
]

app_name = "to-do"
