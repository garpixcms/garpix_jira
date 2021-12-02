from django.db import models
from .server import Server
from .project_category import ProjectCategory


class Project(models.Model):
    project_id = models.IntegerField(default=0, verbose_name='ID проекта')
    project_key = models.CharField(max_length=20, verbose_name='Ключ проекта')
    name = models.CharField(max_length=512, verbose_name='Название')
    server = models.ForeignKey(Server, verbose_name='Сервер Jira', on_delete=models.CASCADE)
    category = models.ForeignKey(ProjectCategory, blank=True, null=True, verbose_name='Категория', on_delete=models.SET_NULL)
    archived = models.BooleanField(default=False, verbose_name='Архивный')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def sync(server: Server):
        jira = server.auth()
        projects = jira.projects()
        categories_dict = {}
        categories = ProjectCategory.objects.all()
        for category in categories:
            categories_dict[category.title] = category
        for project in projects:
            category = None
            if hasattr(project, 'projectCategory'):
                if project.projectCategory.name in categories_dict:
                    category = categories_dict[project.projectCategory.name]
                else:
                    category = ProjectCategory.objects.create(title=project.projectCategory.name)
            project_dict = {
                'project_id': int(project.id),
                'project_key': project.key,
                'name': project.name,
                'server': server,
                'category': category,
                'archived': project.archived,
            }
            obj, created = Project.objects.update_or_create(
                project_id=project.id,
                defaults=project_dict,
            )
