from django.contrib import admin

from .models import Projects

# Register your models here.
@admin.register(Projects)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title', 'author']