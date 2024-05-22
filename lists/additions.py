from lists.models import TypeModel


def get_task_date(tasks):
    items_dates = {}
    for t in tasks:
        date_list = tasks.filter(start_date=t.start_date)
        items_dates[t.start_date] = date_list
    return items_dates


def get_types(user):
    return TypeModel.objects.filter(user_id=user).order_by('type_name')

