from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator
from django.db.models import Q
# For scraping part
import requests
from bs4 import BeautifulSoup
from django.views.generic import CreateView


def news_list(request, *args, **kwargs):
    # fOR scraping part - START **IITG**::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    response = requests.get("http://www.iitg.ac.in/home/eventsall/events")
    soup = BeautifulSoup(response.content,"html.parser")
    cards = soup.find_all("div", attrs={"class": "newsarea"})

    iitg_title = []
    iitg_date = []
    iitg_link = []
    for card in cards[0:6]:
        iitg_date.append(card.find("div", attrs={"class": "ndate"}).text)
        iitg_title.append(card.find("div", attrs={"class": "ntitle"}).text.strip())
        iitg_link.append(card.find("div", attrs={"class": "ntitle"}).a['href'])
    
    
                                    # fOR storing the scraped data directly into the dtatbase from the views.py file - START---------------------------------------------------------------
    for i in range(len(iitg_title)):
        News.objects.get_or_create(
                                    title = iitg_title[i], 
                                    datess = iitg_date[i], 
                                    linkss = iitg_link[i], 
                                    institute_name = "Indian Institute of Technology, Guwahati",
                                    institute_city = "India, Guwhati"
                                    )
                                    # fOR storing the scraped data directly into the dtatbase from the views.py file - END-----------------------------------------------------------------
    # fOR scraping part - END **IITG**::::::::::::::::::::::::::::::::::::::::::::::::::::::::


    # fOR scraping part - START **IITR**::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    response = requests.get("https://www.iitr.ac.in/")
    soup = BeautifulSoup(response.content,"html.parser")
    cardswrapper = soup.find("div", attrs={"class": "wrapper"}) #print(cardswrapper.prettify())
    cardsa = cardswrapper.find_all("a") #print(cardsa)

    iitr_title = []
    iitr_date = []
    iitr_link = []
    for a in cardsa:
        iitr_title.append(a.find("span", attrs={"class": "detailData"}).text)
        iitr_date.append(a.div.text)
        iitr_link.append(a['href'])
    
    # fOR storing the scraped data directly into the dtatbase from the views.py file - START---------------------------------------------------------------
    for i in range(len(iitr_title)):
        News.objects.get_or_create(
                                    title = iitr_title[i], 
                                    datess = iitr_date[i], 
                                    linkss = iitr_link[i], 
                                    institute_name = "Indian Institute of Technology, Rourkee",
                                    institute_city = "India, Roorkee"
                                    )
    # fOR storing the scraped data directly into the dtatbase from the views.py file - END-----------------------------------------------------------------
    # fOR scraping part - END **IITR**::::::::::::::::::::::::::::::::::::::::::::::::::::::::


    queryset = News.objects.all()   #Getting all the objects from the database

    search_query = request.GET.get('q')
    if search_query:
        queryset = queryset.filter(
            Q(title__icontains = search_query) |
            Q(linkss__icontains = search_query)
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


class PostEvent(CreateView):
    model = News
    template_name = 'post_news.html'
    fields = ['title', 'datess', 'institute_name', 'institute_city']