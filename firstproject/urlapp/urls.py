
from django.urls import path
from urlapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.thrid, name='third')
]
