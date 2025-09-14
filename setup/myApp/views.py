# from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

# First view
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")