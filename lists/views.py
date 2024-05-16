import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from lists.forms import ListForm
from lists.models import ListModel
from lists.additions import *


@login_required
def home(request):
    user = request.user
    lists = ListModel.objects.filter(user_id=user, status=False).order_by('start_date', 'start_time')
    items = get_item_date(lists)
    context = {'items': items}
    return render(request, "lists/home.html", context)


@login_required
def today_list(request):
    user = request.user
    lists = ListModel.objects.filter(user_id=user, status=False, start_date=datetime.date.today()).order_by('start_time')
    items = get_item_date(lists)
    context = {'items': items}
    return render(request, "lists/home.html", context)


@login_required
def new_list(request):
    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")
    return render(request, "lists/new_list.html", {"form": form})


@login_required
def list_detail(request, id):
    task = get_object_or_404(ListModel, id=id)
    context = {'item': task}
    return render(request, 'lists/list_detail.html', context)


@login_required
def list_edit(request, id):
    task = get_object_or_404(ListModel, id=id)
    if request.method == "POST":
        form = ListForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('list_detail', id=task.id)
    else:
        form = ListForm(instance=task)
    return render(request, 'lists/list_edit.html', {'form': form})


@login_required
def task_done(request, id):
    task = get_object_or_404(ListModel, id=id)
    task.status = True
    task.save()
    return redirect('home')


@login_required
def task_delete(request, id):
    task = get_object_or_404(ListModel, id=id)
    task.delete()
    return redirect('home')
