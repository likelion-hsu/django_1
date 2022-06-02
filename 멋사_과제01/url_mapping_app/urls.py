from django.urls import path
from url_mapping_app import views


urlpatterns = [
    #path('', views.index),
    path('first/',views.first, name='first'),
    path('second/',views.second, name='second'),
    path('third/',views.third, name='third'),
]