from django.contrib import admin
from django.urls import path
import myapp.home.views as home_views
import myapp.item.views as item_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index, name="index"),
    path('search/', home_views.search, name="search"),
    path('register/<int:id>', home_views.register, name="register"),
    path('delete/<int:id>', home_views.delete, name="delete"),
    path('create-memo/<int:id>', item_views.create, name="memo-create"),
    path('delete-memo/<int:id>', item_views.delete, name="memo-delete")
]
