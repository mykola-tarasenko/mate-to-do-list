from django.urls import path

from to_do.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "to-do"
