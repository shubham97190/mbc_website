from django.db import models
from solo.models import SingletonModel

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="clients", max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order",]


class WebsiteSettings(SingletonModel):
    # Social Media Links
    facebook_link = models.CharField(max_length=200, blank=True)
    twitter_link = models.CharField(max_length=200, blank=True)
    linkedin_link = models.CharField(max_length=200, blank=True)
    instagram_link = models.CharField(max_length=200, blank=True)
    youtube_link = models.CharField(max_length=200, blank=True)

    # App Links
    apple_link = models.CharField(max_length=200, blank=True)
    android_link = models.CharField(max_length=200, blank=True)

    # Other External Links
    accounts_link = models.CharField(max_length=200, blank=True)

    # Enquiry Settings
    enquiries_email = models.CharField(max_length=200)

    # Office 1st
    office_1_name = models.CharField(max_length=255, blank=True)
    office_1_address = models.TextField(blank=True)
    office_1_phone = models.CharField(max_length=255, blank=True)
    office_1_email = models.CharField(max_length=255, blank=True)

    # Office 2nd
    office_2_name = models.CharField(max_length=255, blank=True)
    office_2_address = models.TextField(blank=True)
    office_2_phone = models.CharField(max_length=255, blank=True)
    office_2_email = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "Website Settings"

    class Meta:
        verbose_name = "Website Settings"
        verbose_name_plural = "Website Settings"
