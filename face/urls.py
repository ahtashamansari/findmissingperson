from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('updated/', views.updated, name='updated'),
    path('matched/', views.result, name='matched')
]