from django.contrib import admin


# Register your models here.
class MakerCheckerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'maker', 'checker', 'created_at')
    list_filter = ('status', 'maker', 'checker')
    readonly_fields = ('maker', 'checker', 'created_at', 'updated_at')
    actions = ['request_approval', 'approve_selected', 'reject_selected']
    fieldsets = (
        (None, {
            'fields': ('title','body','status', 'approval_statement','maker', 'checker')
        }),
        ('Dates', {
            'fields': ('created_at','updated_at'),
            'classes': ('collapse',),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.maker = request.user
            obj.status = 'draft'
        super().save_model(request, obj, form, change)

    def request_approval(self, request, queryset):
        rows_updated = queryset.update(status='pending')
        for obj in queryset:
            obj.save()
        self.message_user(request, f"{rows_updated} items marked as pending approval.")
    request_approval.short_description = "Request Approval"

    def approve_selected(self, request, queryset):
        approval_statement = request.POST.get('approval_statement', '') #get approval statement from POST
        rows_updated = 0
        for obj in queryset:
            obj.status = 'approved'
            obj.checker = request.user
            obj.approval_statement = approval_statement
            obj.save()
            rows_updated +=1

        self.message_user(request, f"{rows_updated} items approved.")
    approve_selected.short_description = "Approve selected items"

    def reject_selected(self, request, queryset):
        rows_updated = queryset.update(status='rejected', checker=request.user)
        self.message_user(request, f"{rows_updated} items rejected.")
    reject_selected.short_description = "Reject selected items"

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        if obj and obj.status != 'draft':
            readonly_fields.extend([field.name for field in obj._meta.fields if field.name not in ['status','maker','checker','created_at','updated_at','approval_statement']])
        return readonly_fields

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(maker=request.user) | qs.filter(status='pending') | qs.filter(checker=request.user)
        return qs
