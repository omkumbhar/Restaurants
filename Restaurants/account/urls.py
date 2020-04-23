from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.accountRegistarationView , name = "account-registration" ),
    path('logout/', views.logoutUser , name = "account-logout" ),
    path('login/', views.loginForm , name = "account-login" ),

]