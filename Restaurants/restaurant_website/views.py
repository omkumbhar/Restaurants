from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "restaurant_website/index.html")

def login(request):
    return render(request, "restaurant_website/login.html")

def about(request):
    return render(request, "restaurant_website/about.html")
