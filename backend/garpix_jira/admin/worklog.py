from django.contrib import admin
from ..models.worklog import WorkLog


@admin.register(WorkLog)
class WorkLogAdmin(admin.ModelAdmin):
    list_display = ('worklog_key', 'author', 'time_spent_seconds', 'started_at')
    search_fields = ('author__display_name',)
