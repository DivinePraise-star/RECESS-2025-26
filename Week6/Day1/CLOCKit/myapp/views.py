from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import path
from CLOCKit import views
from CLOCKit.views import index

def index(request):
    return HttpResponse("Hello, World! <br>This is my first Django page, CLOCKit.")