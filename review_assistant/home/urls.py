from django.urls import path

from . import views

urlpatterns = [
    path('home_page/', views.home, name='home_page'),
    path('register/', views.register, name='register'),
]