from django.urls import reverse_lazy
from django.views import generic

from to_do.forms import TaskForm
from to_do.models import Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "to_do/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to-do:index")
