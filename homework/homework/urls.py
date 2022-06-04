from django.contrib import admin
from django.urls import path
from work import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('first', views.first),
    path('second/', views.second),
    path('third', views.third),
    
]
