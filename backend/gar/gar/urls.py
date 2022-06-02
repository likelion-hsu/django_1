from django.contrib import admin
from django.urls import path
from stapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage),
    path('first/',views.firstpage,name = 'firstpage'),
    path('second/', views.secondpage,name = 'secondpage'),
    path('third/', views.thirdpage,name = 'thirdpage')
]
