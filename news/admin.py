from django.contrib import admin

from .models import News
from .models import PageView

admin.site.register(News)
admin.site.register(PageView)
