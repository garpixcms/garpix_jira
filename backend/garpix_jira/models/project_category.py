from django.db import models


class ProjectCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории проектов Jira'
        verbose_name_plural = 'Категории проектов Jira'
        ordering = ('title',)
