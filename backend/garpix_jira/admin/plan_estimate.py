from django.contrib import admin
from ..models.plan_estimate import PlanEstimate


class PlanEstimateInline(admin.TabularInline):
    model = PlanEstimate
    fields = ('specialization', 'time_estimate_seconds', 'created_at')
