from django.urls import reverse_lazy
from django.views import generic

from to_do.forms import TaskForm
from to_do.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "to_do/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to-do:index")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 15


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to-do:tag-list")
