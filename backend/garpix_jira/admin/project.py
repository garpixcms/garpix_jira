from django.contrib import admin
from ..models.project import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_key', 'name', 'server')
    search_fields = ('project_key', 'name')
    readonly_fields = ('project_key', 'name', 'project_id', 'server')
    list_filter = ('server',)
