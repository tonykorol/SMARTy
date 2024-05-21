from django import forms
from lists.models import TaskModel, TypeModel


class TaskForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            queryset = TypeModel.objects.filter(user=user)
            self.fields['task_type'] = forms.ModelChoiceField(queryset=queryset)  # , initial=queryset[0]

    class Meta:
        model = TaskModel
        fields = ("task_name", "task_desc", "start_date", "start_time", "task_type")
        widgets = {
            "task_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter task name"}),
            "task_desc": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter task description"}),
            "start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "start_time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "task_type": forms.Select(attrs={"class": "form-control"}),
        }

        labels = {
            'start_date': 'Select task day',
            'start_time': 'Select task time',
            'task_type': 'Select task type',
        }


class TypeForm(forms.ModelForm):
    class Meta:
        model = TypeModel
        fields = ('type_name',)
        widgets = {
            'type_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter type name"}),
        }
