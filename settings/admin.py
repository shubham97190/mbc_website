from django.contrib import admin
from solo.admin import SingletonModelAdmin
from djboomin.widgets import RichTextEditorWidget
from mbc_website.global_functions import ReadOnlyAdmin
# Register your models here.
from .models import *


class ClientAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'order',]


class AwardAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'order',]


class AsSeenAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'order',]

@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(ReadOnlyAdmin, SingletonModelAdmin):
    formfield_overrides = {models.TextField: {'widget': RichTextEditorWidget}}
    fieldsets = (
        ('Social Media Links', {'fields': ('facebook_link', 'twitter_link','linkedin_link','instagram_link','youtube_link',)}),
        ('App Links', {'fields': ('apple_link', 'android_link',)}),
        ('Other External Links', {'fields': ('accounts_link', 'enquiries_email',)}),
        ('Office 1st', {'fields': ('office_1_name', 'office_1_address','office_1_phone','office_1_email',)}),
        ('Office 2nd', {'fields': ('office_2_name', 'office_2_address','office_2_phone','office_2_email',)}),
    )

admin.site.register(Client, ClientAdmin)
