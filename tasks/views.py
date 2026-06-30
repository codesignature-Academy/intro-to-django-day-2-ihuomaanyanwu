from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to livvy\'s Empire\'s website</h1>')

def about(request):
    return HttpResponse('<h1>we offer wholesome services at livvy\'s Empire</h1>')

def contact(request):
    return HttpResponse('<h1>Contact us through this line:889 livvy\'s Empire</h1>')