from ..models.worklog_table_by_days_page import WorklogTableByDaysPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(WorklogTableByDaysPage)
class WorklogTableByDaysPageAdmin(BasePageAdmin):
    pass
