from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_notification, name='notify'),
    path('shown_notify/<int:id>', views.shown_notification, name='shown_notify'),
]