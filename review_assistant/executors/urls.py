from django.urls import path

from . import views

urlpatterns = [
    path('executors/', views.executors_page, name='executors'),
    path('executor/<int:id>', views.executor_page, name='executor'),
    path('edit_executor/<int:id>', views.edit_executor_page, name='edit_executor'),
    path('delete_executor/<int:id>', views.delete_executor, name='delete_executor'),
    path('create_executor/', views.create_executor_page, name='create_executor'),
]
