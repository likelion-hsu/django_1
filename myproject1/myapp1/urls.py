from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view()),
    path('first/', views.first.as_view()),
    path('second/', views.second.as_view()),
    path('third/', views.third.as_view()),
]