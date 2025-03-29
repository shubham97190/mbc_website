from django.contrib import admin
from django.utils.html import mark_safe

from djboomin.widgets import RichTextEditorWidget
from .models import *


# Register your models here.
from .resource import SeasonMemberResource


@admin.register(Season)
class SeasonPageAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        "name",
        "is_current_active",
        "status",
        "created_date",
        "updated_date",
    ]
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj: Member, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Member)
class MemberPageAdmin(admin.ModelAdmin):
    search_fields = ['name_on_tag', 'email', 'member_color']
    list_display = [
        "name_on_tag",
        "email",
        "name",
        "member_color",
        "level",
        "is_active",
        "created_date",
        "updated_date",
    ]
    readonly_fields = ('created_by', 'updated_by')
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}

    def member_color(self, obj):
        return mark_safe('<div style="width:100%%; height:100%%; background-color:{0};">&nbsp;</div>'.format(obj.color))

    member_color.allow_tags = True

    def save_model(self, request, obj: Member, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


@admin.register(SeasonMemberMapping)
class SeasonMemberPageAdmin(admin.ModelAdmin):
    resource_classes = [SeasonMemberResource]
    search_fields = ['season__name', 'member__name', 'member__name_on_tag']
    list_display = ["get_season_name", "get_member_name", "get_member_name_on_tag", "created_by", "created_date"]
    readonly_fields = ('created_by', 'updated_by')

    @admin.display(description="Season Name", ordering="get_season_name")
    def get_season_name(self, obj):
        return obj.season.name

    @admin.display(description="Member Name", ordering="get_member_name")
    def get_member_name(self, obj):
        return obj.member.name

    @admin.display(description="Name on tag", ordering="get_member_name_on_tag")
    def get_member_name_on_tag(self, obj):
        return obj.member.name_on_tag

    def save_model(self, request, obj: Member, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)
