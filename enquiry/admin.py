from django.contrib import admin
from enquiry.models import Enquiry


# Register your models here.

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'added', ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + (
                'first_name', 'surname', 'email', 'telephone', 'enquirer_type', 'message', 'added', 'ip_address',
            )
        return self.readonly_fields

    def has_add_permission(self, request):
        return False


admin.site.register(Enquiry, EnquiryAdmin)
