from django.db import models
from django.urls import reverse
from solo.models import SingletonModel


class Page(models.Model):
    meta_title = models.CharField(max_length=70)
    meta_description = models.CharField(max_length=160)
    page_banner = models.ImageField(upload_to="banner", blank=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="pages", blank=True)

    class Meta:
        abstract = True


class Home(Page, BaseModel):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"


class About(BaseModel):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"


class Membership(BaseModel, models.Model):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Membership Page"
        verbose_name_plural = "Membership Page"


class FAQ(BaseModel, SingletonModel):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "FAQ Page"
        verbose_name_plural = "FAQ Page"


class GenericPage(BaseModel):
    slug = models.SlugField()
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("page:page", args=[self.slug])

    def __str__(self):
        return self.title


class Blog(BaseModel, SingletonModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Page"


class Contact(Page, SingletonModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return "Contact Page"

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Page"


class HomePageCarousel(models.Model):
    image = models.ImageField(upload_to="homepage", blank=False)
    title = models.CharField(max_length=200, blank=False)
    added_date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
