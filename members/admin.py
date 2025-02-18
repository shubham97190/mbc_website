from django.contrib import admin
from easy_select2 import apply_select2

from djboomin.widgets import RichTextEditorWidget
from .models import *
from django import forms
# Register your models here.
@admin.register(Season)
class SeasonPageAdmin(admin.ModelAdmin):
    list_display = ["name", "is_current_active", "status", "created_date", "updated_date"]
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(Member)
class MemberPageAdmin(admin.ModelAdmin):
    list_display = ["name_on_tag", "email", "name", "color", "level", "is_active", "created_date", "updated_date"]
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(SeasonMemberMapping)
class SeasonMemberPageAdmin(admin.ModelAdmin):
    list_display = [..., 'get_season_name']

    @admin.display(description='Season Name', ordering='get_season_name')
    def get_author_name(self, obj):
        return obj.season.name

    class Meta:
        widgets = {
            'field': apply_select2(forms.Select),
        }
