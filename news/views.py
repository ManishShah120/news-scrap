from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator

def news_list(request):
    queryset = News.objects.all()


    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)


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