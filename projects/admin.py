from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "is_featured", "created_at")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "summary", "tools_used")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("order", "is_featured")
