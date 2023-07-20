from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.tasks_page, name='tasks'),
    path('task/<int:id>', views.task_page, name='task'),
    path('edit_task/<int:id>', views.edit_task_page, name='edit_task'),
]
