from django.contrib import admin
from djboomin.widgets import RichTextEditorWidget
from solo.admin import SingletonModelAdmin
from location.models import Location
from rules.models import Rules

from mbc_website.global_functions import ReadOnlyAdmin
from .models import *


class SingletonPageAdmin(SingletonModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(GenericPage)
class GenericPageAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


admin.site.register(Contact, SingletonPageAdmin)


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(About)
class AboutAdmin(ReadOnlyAdmin, SingletonModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(Membership)
class MembershipAdmin(ReadOnlyAdmin, admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(FAQ)
class FAQAdmin(ReadOnlyAdmin, SingletonModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(Blog)
class BlogAdmin(ReadOnlyAdmin, SingletonModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': RichTextEditorWidget}}


@admin.register(HomePageCarousel)
class HomePageCarouselAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "is_visible", "added_date"]
    formfield_overrides = {models.TextField: {'widget': RichTextEditorWidget}}


@admin.register(Rules)
class RulesAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': RichTextEditorWidget}}
