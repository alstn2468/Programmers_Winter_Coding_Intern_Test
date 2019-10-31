# -*- coding: utf-8 -*-
from myapp.item.models import Item
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404


def check_time(registed_start, registed_end, start, end):
    '''강의 시간 충돌 여부 반환

    Args:
        registed_start : 등록된 강의의 시작 시간
        registed_end   : 등록된 강의의 종료 시간
        start          : 등록할 강의의 시작 시간
        end            : 등록할 강의의 종료 시간

    Returns:
        Boolean: 충돌시  False 반환, 미충돌시 True 반환
    '''
    return registed_start >= end or start >= registed_end


def index(request):
    '''모든 강의 객체와 메인페이지 랜더링

    Args:
        request : 사용자 요청

    Returns:
        모든 강의 객체와 함께 index.html 랜더링
    '''
    items = Item.objects.all()

    return render(request, 'index.html', {
        'items': items,
        'search_items': items
    })


def search(request):
    '''검색 키워드로 필터링된 목록 페이지 랜더링

    Args:
        request : 사용자 요청

    Returns:
        필터링 되지않은 객체, 필터링한 객체, 검색키워드와 index.html 랜더링
    '''
    items = Item.objects.all()
    search_items = items
    keyword = request.GET.get('keyword', '')

    # 강의명, 교수이름, 강의 코드로 필터링 후 강의 코드로 정렬
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
    '''시간표에 강의를 등록

    Args:
        request : 사용자 요청
        id      : 강의의 pk 

    Returns:
        메인 화면으로 redirect
    '''
    items = Item.objects.all()
    item = Item.objects.get(pk=id)

    # 이미 등록된 강의일 경우
    if item.is_register:
        messages.add_message(request, messages.WARNING,
                             "이미 등록된 강의입니다.")

        return redirect("index")

    # 시간 충돌 확인을 위해 시간표에 등록된 강의들을 필터링
    registed_items = Item.objects.all().filter(is_register=True)
    day_of_week = item.day_of_week
    check = True

    # 등록할 강의가 1일 강의할 경우 하나의 요일로 필터링
    if len(day_of_week) == 1:
        qs = registed_items.filter(day_of_week__icontains=day_of_week)

    # 등록할 강의가 2일 강의할 경우 두개의 요일로 필터링
    else:
        qs = registed_items.filter(Q(day_of_week__icontains=day_of_week[0])
                                   | Q(day_of_week__icontains=day_of_week[1]))

    # 필터링한 강의들과 시간 충돌 확인
    for q in qs:
        check = check_time(q.start_time, q.end_time,
                           item.start_time, item.end_time)

        # 이미 충돌이 일어난 경우 반복문 탈출
        if not check:
            break

    # 강의 시간 충돌이 일어나지 않은 경우
    if check:
        item.is_register = not item.is_register
        item.save()
        messages.add_message(request, messages.SUCCESS,
                             "강의를 시간표에 추가 했습니다.")

        return redirect("/")

    # 강의 시간 충돌이 일어난 경우
    messages.add_message(request, messages.ERROR,
                         "시간표에 추가할 수 없는 강의 입니다.")
    return redirect("/")


def delete(request, id):
    '''시간표에서 강의를 삭제

    Args:
        request : 사용자 요청
        id      : 강의의 pk 

    Returns:
        메인 화면으로 redirect
    '''
    try:
        item = Item.objects.get(pk=id)
        item.is_register = not item.is_register

        # 강의와 관계되어 있는 모든 메모들을 삭제
        for memo in item.memos.all():
            memo.delete()

        item.save()
        messages.add_message(request, messages.SUCCESS,
                             "강의를 시간표에서 삭제 했습니다.")

    except Exception as e:
        print(e)
        messages.add_message(request, messages.ERROR,
                             "강의를 시간표에서 삭제하는데 실패 했습니다.")

    return redirect("/")
