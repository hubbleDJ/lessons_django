from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['hello', '111', 'lol']
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'Про нас',
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/about.html', data)