from django.db import models
from django.utils.text import slugify

class News(models.Model):
    title         =   models.CharField(max_length=120)
    datess        =   models.CharField(max_length=120)
    linkss        =   models.CharField(max_length=120)
    entry_date    =   models.DateTimeField(auto_now_add=True)
    slug          =   models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "news"
        ordering = ["-entry_date"]

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f"/news/{self.slug}"