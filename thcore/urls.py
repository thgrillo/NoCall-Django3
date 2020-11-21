from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('send/', views.send_data, name='checkpg'),
]