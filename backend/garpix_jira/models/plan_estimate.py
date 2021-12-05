from django.db import models
from .project_document import ProjectDocument
from .specialization import Specialization
from django.utils import timezone


class PlanEstimate(models.Model):
    specialization = models.ForeignKey(Specialization, verbose_name='Специализация', on_delete=models.CASCADE)
    project_document = models.ForeignKey(ProjectDocument, on_delete=models.CASCADE, verbose_name='Документ')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    time_estimate_seconds = models.IntegerField(default=0, verbose_name='Эстимейт, секунды')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Плановый эстимейт Jira'
        verbose_name_plural = 'Плановые эстимейты Jira'
        ordering = ('-created_at',)
