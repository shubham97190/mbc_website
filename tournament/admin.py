import phonenumber_field.modelfields
from django.contrib import admin
from django import forms
from django.db import models
# Register your models here.
from djboomin.widgets import RichTextEditorWidget
from tournament.models import Tournament, Player, TournamentCategory
from phonenumber_field.widgets import PhoneNumberPrefixWidget


@admin.register(Tournament)
class TournamentPageAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        "name",
        "total_allowed_registration",
        "is_current_active",
        "status",
        "created_date",
        "updated_date",
    ]
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj: Tournament, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Player)
class MemberPageAdmin(admin.ModelAdmin):
    search_fields = ['name', 'partner_name', 'certificate_name', 'certificate_partner_name', 'mobile', 'email']
    list_display = [
        "tournament",
        "get_category_name",
        "name",
        "get_partner_name",
        "updated_by",
        "updated_date"
    ]
    readonly_fields = ('created_by', 'updated_by')
    formfield_overrides = {"mobile": {"widget": PhoneNumberPrefixWidget}}
    list_filter = ["tournament", "category"]

    def save_model(self, request, obj: Player, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    @admin.display(description="Category Name", ordering="get_category_name")
    def get_category_name(self, obj):
        return obj.category.first()

    @admin.display(description="Partner Name", ordering="get_partner_name")
    def get_partner_name(self, obj):
        return obj.partner_name


@admin.register(TournamentCategory)
class TournamentPageAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        "name",
        "fee",
        "tournament",
        "is_active"
    ]
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj: Tournament, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)
