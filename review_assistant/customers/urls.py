from django.urls import path

from . import views

urlpatterns = [
    path('customer/<int:id>', views.customer_page, name='customer'),
    path('customers/', views.customers_page, name='customers'),
    path('create_customer/', views.create_customer_page, name='create_customer'),
    path('edit_customer/<int:id>', views.edit_customer_page, name='edit_customer'),
    path('delete_customer/<int:id>', views.delete_customer, name='delete_customer'),
]
