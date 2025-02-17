from django.contrib import admin
from djboomin.widgets import RichTextEditorWidget
from .models import *
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','published','date',]
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {models.TextField: {'widget': RichTextEditorWidget}}
    