from random import randint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ListForm
from datetime import datetime


LISTS_DATA = [
    {
        "pk": 1,
        "task_name": "Сходить в магазин",
        "task_desc": "Купить хлеб, молоко, пивас",
        "start_time": datetime(2024, 5, 1, 23, 00),
        "type": "Home",
    },
    {
        "pk": 2,
        "task_name": "Созвон с заказчиком",
        "task_desc": "В 12:00 в вайбере",
        "start_time": datetime(2024, 5, 1, 12, 00),
        "type": "Work",
    },
    {
        "pk": 3,
        "task_name": "Сделать домашку",
        "task_desc": "Написать крутую прогу",
        "start_time": None,
        "type": "Education",
    },
    {
        "pk": 4,
        "task_name": "Сделать дичь",
        "task_desc": "Написать крутую прогу",
        "start_time": datetime(2024, 4, 29, 12, 00),
        "type": "Work",
    },
]

DATES_DATA = [datetime(2024, 4, 29, 12, 00), datetime(2024, 5, 1, 23, 00)]


@login_required
def home(request):
    context = {"items": LISTS_DATA, "dates": DATES_DATA}
    return render(request, "lists/home.html", context)


@login_required
def new_list(request):
    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            new_data = {}
            new_data['pk'] = randint(1, 1100)
            new_data = {**form.cleaned_data, **new_data}
            LISTS_DATA.append(new_data)
            return redirect("home")
    return render(request, "lists/new_list.html", {"form": form})


def list_detail(request, pk):
    for i in range(len(LISTS_DATA)):
        for key, value in LISTS_DATA[i].items():
            if value == pk:
                context = {'item': LISTS_DATA[i]}
                return render(request, 'lists/list_detail.html', context)

