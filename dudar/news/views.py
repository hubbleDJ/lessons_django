from django.shortcuts import render

# Create your views here.

def news_home(request):
    data = {
        'title': 'Новости'
    }
    return render(request, 'news/news_home.html', data)