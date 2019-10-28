from django.contrib import admin
from django.urls import path
from myapp.home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('search/', views.serarch, name="search"),
]
