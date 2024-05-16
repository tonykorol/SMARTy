def get_item_date(lists):
    items_dates = {}
    for l in lists:
        date_list = lists.filter(start_date=l.start_date)
        items_dates[l.start_date] = date_list
    return items_dates
