from django.contrib import admin
from django.urls import path
from myapp.home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('search/', views.serarch, name="search"),
    path('register/<int:id>', views.register, name="register"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('detail-lecture/<int:id>',
         views.DetailLectureReadView.as_view(), name="detail_lecture"),
    path('detail-task/<int:id>',
         views.DetailTaskReadView.as_view(), name="detail_task")
]
