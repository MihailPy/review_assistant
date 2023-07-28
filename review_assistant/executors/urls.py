from django.urls import path

from . import views

urlpatterns = [
    path('', views.executors_page, name='executors'),
    path('executor/<int:id>', views.executor_page, name='executor'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile_page, name='edit_profile'),
    path('delete_executor/<int:id>', views.delete_executor, name='delete_executor'),
    path('create_executor/', views.create_executor_page, name='create_executor'),
]
