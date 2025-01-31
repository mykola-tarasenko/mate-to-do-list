from django.views import generic

from to_do.models import Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "to_do/index.html"
