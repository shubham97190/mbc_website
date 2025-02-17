from django.db import models
from page.models import Page
# Create your models here.

class Location(Page, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Location'
