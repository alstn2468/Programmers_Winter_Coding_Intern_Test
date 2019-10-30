# -*- coding: utf-8 -*-
from myapp.item.models import Item
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404


def check_time(registed_start, registed_end, start, end):
    return registed_start >= end or start >= registed_end


def index(request):
    items = Item.objects.all()

    return render(request, 'index.html', {
        'items': items,
        'search_items': items
    })


def search(request):
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

    if item.is_register:
        messages.add_message(request, messages.WARNING,
                             "이미 등록된 강의입니다.")

        return redirect("index")

    registed_items = Item.objects.all().filter(is_register=True)
    day_of_week = item.day_of_week
    check = True

    if len(day_of_week) == 1:
        qs = registed_items.filter(day_of_week__icontains=day_of_week)

    else:
        qs = registed_items.filter(Q(day_of_week__icontains=day_of_week[0])
                                   | Q(day_of_week__icontains=day_of_week[1]))

    for q in qs:
        check = check_time(q.start_time, q.end_time,
                           item.start_time, item.end_time)

        if not check:
            break

    if check:
        item.is_register = not item.is_register
        item.save()
        messages.add_message(request, messages.SUCCESS,
                             "강의를 시간표에 추가 했습니다.")

        return redirect("index")

    messages.add_message(request, messages.ERROR,
                         "시간표에 추가할 수 없는 강의 입니다.")
    return redirect("index")


def delete(request, id):
    try:
        item = Item.objects.get(pk=id)
        item.is_register = not item.is_register

        for memo in item.memos.all():
            memo.delete()

        item.save()
        messages.add_message(request, messages.SUCCESS,
                             "강의를 시간표에서 삭제 했습니다.")

    except Exception as e:
        print(e)
        messages.add_message(request, messages.ERROR,
                             "강의를 시간표에서 삭제하는데 실패 했습니다.")

    return redirect("index")
