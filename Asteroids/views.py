from django.shortcuts import render


# Create your views here.

def index(request):
    variables = {
        "title": "Asteroids",
        "width": 800,
        "height": 600
    }
    return render(request, 'asteroids/index.html', variables)


def menu(request):
    variables = {
        "title": "Asteroids"
    }
    return render(request, 'asteroids/Main-Menu.html', variables)
