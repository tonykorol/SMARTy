from django import forms
from lists.models import ListModel


class ListForm(forms.ModelForm):

    class Meta:
        model = ListModel
        fields = ("list_name", "list_desc", "start_date", "start_time", "list_type")
        widgets = {
            "list_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter task name"}),
            "list_desc": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter task description"}),
            "start_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "start_time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "list_type": forms.Select(attrs={"class": "form-control", "type": "time"}),
        }


