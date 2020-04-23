from django.urls import path
from . import views

urlpatterns = [
     path('bookTable/', views.bookTable, name = "customer-register"),
     path('customerOrders/', views.customerOrder, name = "customer-orders"),

]