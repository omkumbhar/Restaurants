from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'restaurant-home' ),

    path('about/', views.about  , name = 'restaurant-about' ),

    #testing
    path('login2/', views.login  , name = 'restaurant-login' ),
]

