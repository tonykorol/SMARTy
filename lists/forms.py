from django import forms


class ListForm(forms.Form):
    task_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter task name"}
        )
    )
    task_desc = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter task description"}
        ),
        required=False,
    )
    # start_date = forms.DateField(
    #     widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    #     required=False,
    # )
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime"}),
        required=False,
    )
    type_select = forms.NullBooleanField(
        widget=forms.Select(
            choices={'home': "Home", 'work': "Work", 'education': "Education"},
            attrs={"class": "form-select"},
        ),
        required=False,
    )


