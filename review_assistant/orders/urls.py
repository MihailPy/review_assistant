from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.orders_page, name='orders'),
    path('create_order/<int:id>', views.create_order_page, name='create_order'),
    path('edit_order/<int:id>', views.edit_order_page, name='edit_order'),
    path('order/<int:id>', views.order_page, name='order'),
]
