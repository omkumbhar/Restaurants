from django.urls import path
from . import views

urlpatterns = [
    path('addTable/', views.addTable, name = "manager-addTable" ),
    path('home/', views.home , name = "manager-home" ),
    path('AddMenu/', views.addFoodItem , name = "manager-addFoodItem" ),
    path('Orders/', views.viewOrders , name = "manager-viewOrders" ),
    path('Bills/', views.viewBill, name = "manager-viewBill" ),



]