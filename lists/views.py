import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from lists.forms import ListForm, TypeForm
from lists.models import TaskModel, TypeModel
from django.contrib import messages
from lists.additions import get_item_date


@login_required
def home(request, page_name='My Tasks'):
    user = request.user
    lists = TaskModel.objects.filter(user_id=user, status=False).order_by('start_date', 'start_time')
    types = TypeModel.objects.filter(user_id=user).order_by('type_name')
    items = get_item_date(lists)
    context = {'items': items, 'page_name': page_name, 'types': types}
    return render(request, "lists/home.html", context)


@login_required
def today_list(request, page_name='Today Tasks'):
    user = request.user
    lists = TaskModel.objects.filter(user_id=user, status=False, start_date=datetime.date.today()).order_by('start_time')
    types = TypeModel.objects.filter(user_id=user).order_by('type_name')
    items = get_item_date(lists)
    context = {'items': items, 'page_name': page_name, 'types': types}
    return render(request, "lists/home.html", context)


@login_required
def new_list(request):
    user = request.user
    types = TypeModel.objects.filter(user_id=user.id).order_by('type_name')
    form = ListForm(initial={})
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect("home")
    return render(request, "lists/new_list.html", {"form": form, 'types': types})


@login_required
def completed(request):
    user = request.user
    lists = TaskModel.objects.filter(user_id = user, status=True).order_by('start_date', 'start_time')
    types = TypeModel.objects.filter(user_id=user).order_by('type_name')
    items = get_item_date(lists)
    context = {'items': items, 'types': types}
    return render(request, 'lists/completed.html', context)


@login_required
def list_detail(request, id):
    task = get_object_or_404(TaskModel, id=id)
    user = request.user
    types = TypeModel.objects.filter(user_id=user).order_by('type_name')
    context = {'item': task, 'types': types}
    return render(request, 'lists/list_detail.html', context)


@login_required
def list_edit(request, id):
    task = get_object_or_404(TaskModel, id=id)
    user = request.user
    types = TypeModel.objects.filter(user_id=user).order_by('type_name')
    if request.method == "POST":
        form = ListForm(request.POST, instance=task)
        if form.is_valid():
            if task.status == True:
                task.status = False
                messages.add_message(request, messages.INFO, f"The '{task.list_name}' task has been restored")
            else:
                messages.add_message(request, messages.INFO, f"The '{task.list_name}' task has been edited")
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('list_detail', id=task.id)
    else:
        form = ListForm(instance=task)
    return render(request, 'lists/list_edit.html', {'form': form, 'types': types})


@login_required
def task_done(request, id):
    task = get_object_or_404(TaskModel, id=id)
    task.status = True
    task.save()
    messages.add_message(request, messages.INFO, f"'{task.list_name}' task complete")
    return redirect('home')


@login_required
def task_delete(request, id):
    task = get_object_or_404(TaskModel, id=id)
    task.delete()
    messages.add_message(request, messages.INFO, f"The '{task.list_name}' task has been deleted")
    return redirect('home')


@login_required
def type_filter(request, t_filter):
    user = request.user
    list_type = get_object_or_404(TypeModel, type_name=t_filter)
    lists = TaskModel.objects.filter(user_id=user, status=False, list_type=list_type).order_by('start_date', 'start_time')
    types = TypeModel.objects.filter(user_id=user).order_by('type_name')
    items = get_item_date(lists)
    page_name = f"My '{t_filter}' tasks"
    context = {'items': items, 'types': types, 'page_name': page_name}
    return render(request, 'lists/home.html', context)


@login_required
def new_type(request):
    form = TypeForm()
    previous_page = request.GET.get('next') if request.GET.get('next') is not None else ''
    user = request.user
    types = TypeModel.objects.filter(user_id=user).order_by('type_name')
    if request.method == "POST":
        form = TypeForm(request.POST)
        if form.is_valid():
            new_type = form.save(commit=False)
            new_type.user = user
            new_type.save()
            return redirect(previous_page) if previous_page != '' else redirect('home')
        messages.add_message(request, messages.ERROR, f"This type already exists")
    return render(request, 'lists/new_type.html', {'form': form, 'types': types})
