from django import forms
from lists.models import TaskModel, TypeModel


class ListForm(forms.ModelForm):

    class Meta:
        model = TaskModel
        fields = ("list_name", "list_desc", "start_date", "start_time", "list_type")
        widgets = {
            "list_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter task name"}),
            "list_desc": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter task description"}),
            "start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "start_time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "list_type": forms.Select(attrs={"class": "form-control", "type": "time"}),
        }

        labels = {
            'start_date': 'Select task day',
            'start_time': 'Select task time',
            'list_type': 'Select task type',
        }


class TypeForm(forms.ModelForm):

    class Meta:
        model = TypeModel
        fields = ('type_name', )
        widgets = {
            'type_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter type name"}),
        }
