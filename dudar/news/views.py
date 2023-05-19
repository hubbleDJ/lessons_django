from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArtclesForm

def news_home(request):
    data = {
        'title': 'Новости',
        'news': Articles.objects.order_by('-date')
    }
    return render(request, 'news/news_home.html', data)


def create(request):
    data = {'title': 'Форма для добавления статьи'}

    if request.method == 'POST':
        data['form'] = ArtclesForm(request.POST)
        if data['form'].is_valid():
            data['form'].save()
            data['error'] = 'Статья сохранена'
            return redirect('home')
        else:
            data['error'] = 'Неверно заполнено'

    else: data['form'] = ArtclesForm()

    return render(request, 'news/create.html', data)