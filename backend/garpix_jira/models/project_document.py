from django.db import models
from .project import Project
from django.utils import timezone
from garpix_utils.file.file_field import get_file_path


class ProjectDocument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    file = models.FileField(upload_to=get_file_path, verbose_name='Файл', blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Документ для проекта Jira'
        verbose_name_plural = 'Документы для проектов Jira'
        ordering = ('-created_at',)
