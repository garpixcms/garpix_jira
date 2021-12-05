from django.contrib import admin
from ..models.project_document import ProjectDocument
from .plan_estimate import PlanEstimateInline


@admin.register(ProjectDocument)
class ProjectDocumentAdmin(admin.ModelAdmin):
    list_display = ('project', 'created_at', 'file')
    inlines = (PlanEstimateInline,)
