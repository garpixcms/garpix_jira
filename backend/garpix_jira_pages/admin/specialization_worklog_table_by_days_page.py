from ..models.specialization_worklog_table_by_days_page import SpecializationWorklogTableByDaysPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(SpecializationWorklogTableByDaysPage)
class SpecializationWorklogTableByDaysPageAdmin(BasePageAdmin):
    pass
