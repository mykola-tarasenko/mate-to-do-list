from django import forms

from to_do.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "is_done", "tags")
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                },
            ),
            "tags": forms.CheckboxSelectMultiple(),
        }