from django.contrib import admin

from .models import Education, Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date", "order")
    search_fields = ("company", "role")
    list_editable = ("order",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_date", "end_date", "order")
    search_fields = ("institution", "degree")
    list_editable = ("order",)
