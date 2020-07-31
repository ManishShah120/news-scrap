from django.shortcuts import render
from .models import News

def news_list(request):
    queryset = News.objects.all()
    context = {
       'object_list': queryset
    }
    return render(request, 'news_list.html', context)


def dynamic_lookup_view(request, news_slug):
    obj = News.objects.get(slug=news_slug)
    context = {
        "object":obj
    }
    return render(request, 'news_detail.html', context)