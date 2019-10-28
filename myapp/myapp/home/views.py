from django.shortcuts import render
from ..item.models import Item


def index(request):
    items = Item.objects.all()

    return render(request, 'index.html', {'items': items})


def serarch(request):
    items = Item.objects.all()
    keyword = request.GET.get('keyword', '')

    if keyword:
        items = items.filter(lecture__icontains=keyword)

    return render(request, 'index.html', {
        'items': items,
        'keyword': keyword,
    })
