from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Item, Memo
from .forms import MemoForm


def create(request, id):
    '''메모를 생성하는 함수

    Args:
        request: 메모 Form 데이터
        id     : 강의의 pk

    Returns:
        redirect: 메모 생성,성공 실패 모두 메세지와 홈화면 이동
    '''
    item = get_object_or_404(Item, pk=id)

    try:
        if request.method == "POST":
            form = MemoForm(request.POST)

            # Form 데이터 유효성 검증 후 강의 정보 fk 저장
            if form.is_valid():
                memo = form.save(commit=False)
                memo.item = item
                memo.save()

                messages.add_message(
                    request, messages.SUCCESS, "메모 추가에 성공했습니다.")

                return redirect("/")

    except Exception as e:
        print("Exception :", e)
        messages.add_message(request, messages.ERROR, "메모 추가에 실패했습니다.")

    return redirect("/")


def delete(request, id):
    '''메모를 삭제하는 함수

    Args:
        request : 메모 Form 데이터
        id      : 메모의 pk

    Returns:
        redirect: 메모 삭제,성공 실패 모두 메세지와 홈화면으로 이동
    '''
    try:
        memo = get_object_or_404(Memo, pk=id)
        memo.delete()

        messages.add_message(request, messages.SUCCESS, "메모 삭제에 성공했습니다.")

    except Exception as e:
        print("Exception :", e)
        messages.add_message(request, messages.ERROR, "메모 삭제에 실패했습니다.")

    return redirect("/")
