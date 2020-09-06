from django.urls import path
from .views import (
    news_list,
    dynamic_lookup_view,
    PostEvent
)

urlpatterns = [
    path("", news_list, name="news_list"),
    path("post_create/", PostEvent.as_view(success_url='/news'), name="post_event"),
    path("<slug:news_slug>", dynamic_lookup_view, name="news_detail"),
]