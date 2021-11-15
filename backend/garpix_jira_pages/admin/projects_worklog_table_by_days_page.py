from ..models.projects_worklog_table_by_days_page import ProjectsWorklogTableByDaysPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(ProjectsWorklogTableByDaysPage)
class ProjectsWorklogTableByDaysPageAdmin(BasePageAdmin):
    pass
