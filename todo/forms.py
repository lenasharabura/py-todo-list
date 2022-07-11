import datetime

from django import forms
from django.forms import DateTimeInput

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]

        if deadline and deadline < datetime.datetime.today():
            raise forms.ValidationError("Deadline must be in the future!")
        return deadline

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
