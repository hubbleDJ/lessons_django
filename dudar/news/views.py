from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Articles
from .forms import ArtclesForm



def news_home(request):
    data = {
        'title': 'Новости',
        'news': Articles.objects.order_by('-date')
    }
    return render(request, 'news/news_home.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdatelView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    context_object_name = 'article'
    form_class = ArtclesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news_delete.html'

def create(request):
    data = {'title': 'Форма для добавления статьи'}

    if request.method == 'POST':
        data['form'] = ArtclesForm(request.POST)
        if data['form'].is_valid():
            data['form'].save()
            data['error'] = 'Статья сохранена'
            return redirect('news_home')
        else:
            data['error'] = 'Неверно заполнено'

    else: data['form'] = ArtclesForm()

    return render(request, 'news/create.html', data)
