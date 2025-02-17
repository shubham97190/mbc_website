from django.contrib import admin
from djboomin.widgets import RichTextEditorWidget
from .models import *
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': RichTextEditorWidget}}

admin.site.register(Question,QuestionAdmin)