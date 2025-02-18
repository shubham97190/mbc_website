from django.contrib import admin

from djboomin.widgets import RichTextEditorWidget
from .models import *


# Register your models here.
@admin.register(Season)
class SeasonPageAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_current_active",
        "status",
        "created_date",
        "updated_date",
    ]
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}


@admin.register(Member)
class MemberPageAdmin(admin.ModelAdmin):
    list_display = [
        "name_on_tag",
        "email",
        "name",
        "color",
        "level",
        "is_active",
        "created_date",
        "updated_date",
    ]
    readonly_fields = ('created_by', 'updated_by')
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}

    def save_model(self, request, obj: Member, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


@admin.register(SeasonMemberMapping)
class SeasonMemberPageAdmin(admin.ModelAdmin):
    list_display = ["get_season_name",]

    @admin.display(description="Season Name", ordering="get_season_name")
    def get_season_name(self, obj):
        return obj.season.name
