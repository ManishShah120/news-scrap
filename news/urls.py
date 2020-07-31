from django.urls import path
from .views import (
    news_list,
    dynamic_lookup_view
)

urlpatterns = [
    path('', news_list, name='news_list'),
    path('<slug:news_slug>', dynamic_lookup_view, name='news_detail'),
]