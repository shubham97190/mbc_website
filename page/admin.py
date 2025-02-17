from django.contrib import admin
from djboomin.widgets import RichTextEditorWidget
from solo.admin import SingletonModelAdmin
from location.models import Location

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
class HomeAdmin(ReadOnlyAdmin, SingletonModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    fieldsets = (
        (
            "Meta Information",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "page_banner",
                )
            },
        ),
        (
            "Plan Enterprise Solutions",
            {
                "fields": (
                    "section_1_title",
                    "section_1_description",
                    "section_1_image",
                    "section_1_more_button_link",
                )
            },
        ),
        (
            "CASE STUDY",
            {
                "fields": (
                    "section_2_part_1_image",
                    "section_2_part_1_title",
                    "section_2_part_1_description",
                    "section_2_part_1_more_button_link",
                    "section_2_part_2_image",
                    "section_2_part_2_title",
                    "section_2_part_2_description",
                    "section_2_part_2_more_button_link",
                    "section_2_part_3_image",
                    "section_2_part_3_title",
                    "section_2_part_3_description",
                    "section_2_part_3_more_button_link",
                    "section_2_part_4_image",
                    "section_2_part_4_title",
                    "section_2_part_4_description",
                    "section_2_part_4_more_button_link",
                )
            },
        ),
        ("Helps you Find", {"fields": ("section_3_title",)}),
    )


@admin.register(About)
class AboutAdmin(ReadOnlyAdmin, SingletonModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    fieldsets = (
        (
            "Meta Information",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "page_banner",
                )
            },
        ),
        (
            "Section one",
            {"fields": ("section_1_title", "section_1_image", "section_1_description")},
        ),
        (
            "Section two",
            {
                "fields": (
                    "section_2_image",
                    "section_2_content_1",
                    "section_2_content_2",
                )
            },
        ),
    )


@admin.register(Membership)
class MembershipAdmin(ReadOnlyAdmin, admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    fieldsets = (
        (
            "Meta Information",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "page_banner",
                )
            },
        ),
        ("Section", {"fields": ("title", "image_1", "image_2", "description")}),
    )


@admin.register(FAQ)
class FAQAdmin(ReadOnlyAdmin, SingletonModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    fieldsets = (
        (
            "Meta Information",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "page_banner",
                )
            },
        ),
        ("Information", {"fields": ("title", "description")}),
    )


@admin.register(Blog)
class BlogAdmin(ReadOnlyAdmin, SingletonModelAdmin):
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    fieldsets = (
        (
            "Meta Information",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "page_banner",
                )
            },
        ),
        ("Heading Section", {"fields": ("title", "description")}),
    )
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': RichTextEditorWidget}}
