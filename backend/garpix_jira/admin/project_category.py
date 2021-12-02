from django.contrib import admin
from ..models.project_category import ProjectCategory


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
