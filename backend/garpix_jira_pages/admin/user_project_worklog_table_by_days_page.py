from ..models.user_project_worklog_table_by_days_page import UserProjectWorklogTableByDaysPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(UserProjectWorklogTableByDaysPage)
class UserProjectWorklogTableByDaysPageAdmin(BasePageAdmin):
    pass
