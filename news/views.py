from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator
from django.db.models import Q

def news_list(request):
    queryset = News.objects.all()   #Getting all the objects from the database

    search_query = request.GET.get('q')
    if search_query:
        queryset = queryset.filter(
            Q(title__icontains = search_query) |
            Q(description__icontains = search_query)
        )

    paginator = Paginator(queryset, 5)  #Adding pagination
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