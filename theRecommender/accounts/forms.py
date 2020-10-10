from django import forms
from .models import Tasks

forms.DateInput.input_type = "date"
forms.DateTimeInput.input_type = "datetime-local"


class CreateTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'task',
            'deadline'
        ]

    def __init__(self, *args, **kwargs):
        super(CreateTask, self).__init__(*args, **kwargs)
        self.fields['task'].widget.attrs.update({'type':'text', 'class':'form-control', 'id':'validationTooltip03', 'name':'input_task', 'placeholder': 'What is your task!', 'required':'True'})
        self.fields['deadline'].widget.attrs.update({'class':'form-control', 'name':'input_deadline', 'id':'validationTooltip04', 'required':'True'})

    def save(self, user, commit=True):
        task = super(CreateTask, self).save(commit=False)
        task.user = user
        if commit:
            task.save()
        return task
