from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Item, Memo
from .forms import MemoForm


@csrf_exempt
def create(request, id):
    item = get_object_or_404(Item, pk=id)
    items = Item.objects.all()

    if request.method == "GET":
        form = MemoForm(request.GET)

        if form.is_valid():
            memo = form.save(commit=False)
            memo.item = item
            memo.save()

            messages.add_message(request, messages.SUCCESS, "메모 추가에 성공했습니다.")

            return redirect("/")

    messages.add_message(request, messages.ERROR, "메모 추가에 실패했습니다.")

    return redirect("/")


@csrf_exempt
def delete(request, id):
    try:
        memo = get_object_or_404(Memo, pk=id)
        items = Item.objects.all()
        memo.delete()

        messages.add_message(request, messages.SUCCESS, "메모 삭제에 성공했습니다.")

    except:
        messages.add_message(request, messages.ERROR, "메모 삭제에 실패했습니다.")

    return redirect("/")
