from django.shortcuts import render
from .models import News

def news_list(request):
    queryset = News.objects.all()
    context = {
       'object_list': queryset
    }
    return render(request, 'news_list.html', context)


def dynamic_lookup_view(request, id):
    obj = News.objects.get(id=id)
    context = {
        "object":obj
    }
    return render(request, 'news_detail.html', context)