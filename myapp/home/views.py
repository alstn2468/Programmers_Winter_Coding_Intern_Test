from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from ..item.models import Item
from django.db.models import Q
from django.contrib import messages
from bootstrap_modal_forms.generic import BSModalReadView


def check_time(registed_start, registed_end, start, end):
    return True


def index(request):
    items = Item.objects.all()

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
    check = True

    for registed_item in registed_items:
        for day in day_of_week:
            if day in registed_item.day_of_week:
                check = check_time(registed_item.start_time, registed_item.end_time,
                                   item.start_time, item.end_time)

        if not check:
            break

    if check and not item.is_register:
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
        item.save()
        messages.add_message(request, messages.SUCCESS,
                             "강의를 시간표에서 삭제 했습니다.")

    except:
        messages.add_message(request, messages.ERROR,
                             "강의를 시간표에서 삭제하는데 실패 했습니다.")

    return redirect("index")


class DetailLectureReadView(BSModalReadView):
    model = Item


class DetailTaskReadView(BSModalReadView):
    model = Item
