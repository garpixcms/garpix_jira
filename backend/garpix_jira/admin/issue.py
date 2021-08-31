from django.contrib import admin
from ..models.issue import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_key', 'name', 'assignee', 'creator', 'reporter', 'created_at', 'project')
    search_fields = ('issue_key', 'name', 'content')
    list_filter = ('project',)
    readonly_fields = ('issue_key', 'name', 'assignee', 'creator', 'reporter', 'created_at',
                       'project', 'content', 'due_date')
