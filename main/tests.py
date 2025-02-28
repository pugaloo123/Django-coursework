from django.http import HttpRequest
from django.shortcuts import render

# Create your tests here.
def index(request):
    return HttpRequest('Home page')

def about(request):
    return HttpRequest('About page')

