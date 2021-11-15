from django.db import models


class Specialization(models.Model):
    title = models.CharField(blank=True, default='', max_length=128, verbose_name='Отображаемое имя')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ('title',)

    def __str__(self):
        return self.title
