from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ListForm


@login_required
def home(request):
    return render(request, "lists/home.html")


@login_required
def new_list(request):
    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("home")
    return render(request, "lists/new_list.html", {"form": form})
