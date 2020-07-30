from django.db import models

class News(models.Model):
    title       =   models.CharField(max_length=120)
    description =   models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return f"/news/{self.id}/"
    