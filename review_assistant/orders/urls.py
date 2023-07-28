from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.orders_page, name='orders'),
    path('create_order/<int:id>', views.create_order_page, name='create_order'),
    path('edit_order/<int:id>', views.edit_order_page, name='edit_order'),
    path('order/<int:id>', views.order_page, name='order'),
    path('edit_img/<int:id>', views.edit_img, name='edit_img'),
    path('delete_img/<int:id>', views.delete_img, name='delete_img'),
    path('divide_into_tasks/<int:id>', views.divide_into_tasks, name='divide_into_tasks'),
]
