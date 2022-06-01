from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view()),
    path('first/', views.First.as_view()),
    path('second/', views.Second.as_view()),
    path('third/', views.Third.as_view()),
]