from django.contrib import admin
from .models import Post

from django import forms
from ckeditor.widgets import CKEditorWidget


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']