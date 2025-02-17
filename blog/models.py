from datetime import datetime
from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    lead = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="blog/post", blank=True)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return reverse('page:blog-detail', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
