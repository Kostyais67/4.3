from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):

    model = News

    ordering = '-publication_date'

    template_name = 'newst.html'

    context_object_name = 'news'


class NewsDetail(DetailView):

    model = News

    template_name = 'news.html'

    context_object_name = 'news'
