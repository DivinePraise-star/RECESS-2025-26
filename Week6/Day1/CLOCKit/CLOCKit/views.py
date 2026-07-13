#view library
from django.http import HttpResponse
from django.urls import path
from CLOCKit import views

def index(request):
    return HttpResponse("Hello, World! <br>This is my first Django page, CLOCKit.")