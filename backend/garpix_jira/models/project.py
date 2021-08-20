from django.db import models
from .server import Server


class Project(models.Model):
    project_id = models.IntegerField(default=0, verbose_name='ID проекта')
    project_key = models.CharField(max_length=20, verbose_name='Ключ проекта')
    name = models.CharField(max_length=512, verbose_name='Название')
    server = models.ForeignKey(Server, verbose_name='Сервер Jira', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def sync(server: Server):
        jira = server.auth()
        projects = jira.projects()
        for project in projects:
            project_dict = {
                'project_id': int(project.id),
                'project_key': project.key,
                'name': project.name,
                'server': server,
            }
            obj, created = Project.objects.update_or_create(
                project_id=project.id,
                defaults=project_dict,
            )
