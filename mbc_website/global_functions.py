from django.contrib import admin

class ReadOnlyAdmin(object):

    # change_form_template = "admin/view.html"

    def get_actions(self, request):
        actions = super(ReadOnlyAdmin, self).get_actions(request)
        if request.user.has_perm('members.read_only_admin') and not request.user.is_superuser:
            return []
        return actions

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        if request.user.has_perm('members.read_only_admin') and not request.user.is_superuser:
            extra_context['show_save_and_continue'] = False
            extra_context['show_save'] = False
        return super(ReadOnlyAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def has_add_permission(self, request):
        if request.user.has_perm('members.read_only_admin') and not request.user.is_superuser:
            return False
        else:
            return super(ReadOnlyAdmin, self).has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('members.read_only_admin') and not request.user.is_superuser:
            return False
        else:
            return super(ReadOnlyAdmin, self).has_delete_permission(request)

    def save_model(self, request, obj, form, change):
        if request.user.has_perm('members.read_only_admin') and not request.user.is_superuser:
            pass
        else:
            return super(ReadOnlyAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if request.user.has_perm('members.read_only_admin') and not request.user.is_superuser:
            pass
        else:
            return super(ReadOnlyAdmin, self).delete_model(request, obj)

    def save_related(self, request, form, formsets, change):
        if request.user.has_perm('members.read_only_admin') and not request.user.is_superuser:
            pass
        else:
            return super(ReadOnlyAdmin, self).save_model(request, form, formsets, change)