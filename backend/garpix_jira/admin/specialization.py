from django.contrib import admin
from ..models.specialization import Specialization


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('title',)
