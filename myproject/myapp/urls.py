from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('1', views.first),
    path('2', views.second),
    path('3', views.third),
]