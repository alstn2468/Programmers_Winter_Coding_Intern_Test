from django.shortcuts import render, redirect
from ..item.models import Item
from django.db.models import Q


def check_time(registed_start, registed_end, start, end):
    return True


def index(request):
    items = Item.objects.all()
    print(items.filter(is_register=True))

    return render(request, 'index.html', {
        'items': items,
        'search_items': items
    })


def serarch(request):
    items = Item.objects.all()
    search_items = items
    keyword = request.GET.get('keyword', '')

    if keyword:
        search_items = items.filter(Q(lecture__icontains=keyword)
                                    | Q(professor__icontains=keyword)
                                    | Q(lecture_code__icontains=keyword)).order_by("lecture_code")

    return render(request, 'index.html', {
        'items': items,
        'search_items': search_items,
        'keyword': keyword,
    })


def register(request, id):
    items = Item.objects.all()
    item = Item.objects.get(pk=id)
    registed_items = Item.objects.all().filter(is_register=True)
    day_of_week = item.day_of_week

    for registed_item in registed_items:

        if len(day_of_week) == 1 \
                and len(registed_item.day_of_week) == 1:
            if day_of_week == registed_item.day_of_week:
                check = check_time(registed_item.start_time,
                                   registed_item.end_time,
                                   item.start_time,
                                   item.end_time)

        elif len(day_of_week) == 1 \
                and len(registed_item.day_of_week) == 2:
            if day_of_week in registed_item.day_of_week:
                check = check_time(registed_item.start_time,
                                   registed_item.end_time,
                                   item.start_time,
                                   item.end_time)

        elif len(day_of_week) == 2 \
                and len(registed_item.day_of_week) == 1:
            if registed_item.day_of_week in day_of_week:
                check = check_time(registed_item.start_time,
                                   registed_item.end_time,
                                   item.start_time,
                                   item.end_time)

        else:
            if day_of_week[0] in registed_item.day_of_week \
                    or day_of_week[1] in registed_item.day_of_week:
                check = check_time(registed_item.start_time,
                                   registed_item.end_time,
                                   item.start_time,
                                   item.end_time)

    if check:
        item.is_register = not item.is_register
        item.save()

    return redirect("index")


def delete(request, id):
    item = Item.objects.get(pk=id)
    item.is_register = not item.is_register
    item.save()

    return redirect("index")
