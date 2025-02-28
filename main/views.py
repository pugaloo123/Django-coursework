
from django.http import HttpResponse
from django.shortcuts import render

# Create your tests here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home',
        'is_authenticated': False,
        'info': 'Nikita'
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    return HttpResponse('About page')