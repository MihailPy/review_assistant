from django.urls import path

from . import views

urlpatterns = [
    path('', views.tasks_page, name='tasks'),
    path('task/<int:id>', views.task_page, name='task'),
    path('confirm_correspondence/<int:id>', views.confirm_correspondence, name='confirm_correspondence'),
    path('confirm_execution/<int:id>', views.confirm_execution, name='confirm_execution'),
    path('add_image/<int:id>', views.add_image, name='add_image'),
    path('edit_task/<int:id>', views.edit_task_page, name='edit_task'),
]
