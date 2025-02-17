from django.db import models
from solo.models import SingletonModel
from django.urls import reverse


class Page(models.Model):
    meta_title = models.CharField(max_length=70)
    meta_description = models.CharField(max_length=160)
    page_banner = models.ImageField(upload_to="banner", blank=True)

    class Meta:
        abstract = True


class Home(Page, SingletonModel):
    # Plan Enterprise Solutions
    section_1_title = models.CharField(max_length=255)
    section_1_description = models.TextField()
    section_1_image = models.ImageField(upload_to="home", blank=True)
    section_1_more_button_link = models.CharField(max_length=255, blank=True)

    # CASE STUDY
    section_2_part_1_image = models.ImageField(upload_to="home", blank=True)
    section_2_part_1_title = models.CharField(max_length=255)
    section_2_part_1_description = models.TextField(blank=True)
    section_2_part_1_more_button_link = models.CharField(max_length=255, blank=True)

    section_2_part_2_image = models.ImageField(upload_to="home", blank=True)
    section_2_part_2_title = models.CharField(max_length=255)
    section_2_part_2_description = models.TextField(blank=True)
    section_2_part_2_more_button_link = models.CharField(max_length=255, blank=True)

    section_2_part_3_image = models.ImageField(upload_to="home", blank=True)
    section_2_part_3_title = models.CharField(max_length=255)
    section_2_part_3_description = models.TextField(blank=True)
    section_2_part_3_more_button_link = models.CharField(max_length=255, blank=True)

    section_2_part_4_image = models.ImageField(upload_to="home", blank=True)
    section_2_part_4_title = models.CharField(max_length=255)
    section_2_part_4_description = models.TextField(blank=True)
    section_2_part_4_more_button_link = models.CharField(max_length=255, blank=True)

    section_3_title = models.CharField(max_length=255)

    def __str__(self):
        return "Home"

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"


class About(Page, SingletonModel):
    # Section one
    section_1_title = models.CharField(max_length=255)
    section_1_description = models.TextField()
    section_1_image = models.ImageField(upload_to="aboutus", blank=True)

    # Section Two
    section_2_image = models.ImageField(upload_to="aboutus", blank=True)
    section_2_content_1 = models.TextField()
    section_2_content_2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return "About Page"

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"


class Membership(Page, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_1 = models.ImageField(upload_to="membership", blank=True)
    image_2 = models.ImageField(upload_to="membership", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Membership Page"
        verbose_name_plural = "Membership Page"


class FAQ(Page, SingletonModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "FAQ Page"
        verbose_name_plural = "FAQ Page"


class GenericPage(Page):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("page:page", args=[self.slug])

    def __str__(self):
        return self.title


class Blog(Page, SingletonModel):
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


class HomePageCarousel(Page, SingletonModel):
    section_2_image = models.ImageField(upload_to="aboutus", blank=True)
