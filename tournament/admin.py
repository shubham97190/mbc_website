from django.contrib import admin
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
# Register your models here.
from import_export.admin import ExportActionModelAdmin
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms.widgets import Select, TextInput

from djboomin.widgets import RichTextEditorWidget
from tournament.models import Tournament, Player, TournamentCategory, TournamentWinnerPage
from tournament.resource import PlayerResource


class TournamentFilter(admin.SimpleListFilter):
    title = "Tournament"
    parameter_name = "by_tournament"

    def lookups(self, request, model_admin):
        return [("all", "All Tournaments")] + [
            (t.pk, str(t))
            for t in Tournament.objects.all().order_by("-created_date")
        ]

    def queryset(self, request, queryset):
        if self.value() == "all":
            return queryset
        if self.value():
            return queryset.filter(tournament__pk=self.value())
        return queryset


class ActiveEventCategoryFilter(admin.SimpleListFilter):
    title = "Category (active event)"
    parameter_name = "active_category"

    def lookups(self, request, model_admin):
        active_tournament = Tournament.objects.filter(is_current_active=True).first()
        if not active_tournament:
            return []
        return [
            (cat.pk, str(cat))
            for cat in TournamentCategory.objects.filter(tournament=active_tournament).order_by("name")
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__pk=self.value())
        return queryset


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
    actions = ['duplicate_tournament']

    def save_model(self, request, obj: Tournament, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    @admin.action(description="Duplicate selected tournament (with categories)")
    def duplicate_tournament(self, request, queryset):
        if queryset.count() != 1:
            self.message_user(request, "Please select exactly one tournament to duplicate.", level="error")
            return
        original = queryset.first()
        categories = list(TournamentCategory.objects.filter(tournament=original))

        original.pk = None
        original.name = f"{original.name} (Copy)"
        original.title = f"{original.title} (Copy)"
        original.is_current_active = False
        original.created_by = request.user
        original.updated_by = request.user
        original.save()

        for cat in categories:
            cat.pk = None
            cat.tournament = original
            cat.created_by = request.user
            cat.updated_by = request.user
            cat.save()

        self.message_user(
            request,
            f'Tournament "{original.name}" duplicated with {len(categories)} categories.',
        )


@admin.register(Player)
class MemberPageAdmin(ExportActionModelAdmin):
    resource_classes = [PlayerResource]
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
    list_filter = [TournamentFilter, ActiveEventCategoryFilter]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Default to active tournament when no tournament filter is explicitly set
        if 'by_tournament' not in request.GET:
            active = Tournament.objects.filter(is_current_active=True).first()
            if active:
                return qs.filter(tournament=active)
        return qs

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'mobile' in form.base_fields:
            form.base_fields['mobile'].widget = PhoneNumberPrefixWidget(widgets=(Select, TextInput))
        return form

    def save_model(self, request, obj: Player, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    def send_email_for_payment(self, request, queryset):
        message_bit = queryset.count()
        self.message_user(request, f"{message_bit} successfully email sent.")

    @admin.display(description="Category Name", ordering="get_category_name")
    def get_category_name(self, obj):
        return obj.category.first()

    @admin.display(description="Partner Name", ordering="get_partner_name")
    def get_partner_name(self, obj):
        return obj.partner_name

    send_email_for_payment.short_description = "Send Email for payment selected Players"
    actions = [send_email_for_payment]


@admin.register(TournamentCategory)
class TournamentCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        "name",
        "fee",
        "tournament",
        "is_active"
    ]
    list_filter = ["tournament"]
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
    readonly_fields = ('created_by', 'updated_by')
    actions = ['copy_to_active_tournament', 'duplicate_categories']

    def save_model(self, request, obj: TournamentCategory, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    @admin.action(description="Copy selected categories to active tournament")
    def copy_to_active_tournament(self, request, queryset):
        active = Tournament.objects.filter(is_current_active=True).first()
        if not active:
            self.message_user(request, "No active tournament found.", level="error")
            return
        count = 0
        for cat in queryset.exclude(tournament=active):
            cat.pk = None
            cat.tournament = active
            cat.created_by = request.user
            cat.updated_by = request.user
            cat.save()
            count += 1
        self.message_user(request, f"{count} categories copied to '{active.name}'.")

    @admin.action(description="Duplicate selected categories (within same tournament)")
    def duplicate_categories(self, request, queryset):
        count = 0
        for cat in queryset:
            cat.pk = None
            cat.name = f"{cat.name} (Copy)"
            cat.code = f"{cat.code}_c"
            cat.created_by = request.user
            cat.updated_by = request.user
            cat.save()
            count += 1
        self.message_user(request, f"{count} categories duplicated.")


@admin.register(TournamentWinnerPage)
class TournamentWinnerPageAdmin(admin.ModelAdmin):
    list_display = ["title", "tournament", "is_published", "updated_date"]
    list_filter = ["is_published", "tournament"]
    search_fields = ["title", "tournament__name"]
    list_editable = ["is_published"]
    formfield_overrides = {models.TextField: {"widget": RichTextEditorWidget}}
