from django.db import models
from .user import User
from .project import Project
from .server import Server
import time


class Issue(models.Model):
    issue_key = models.CharField(max_length=50, verbose_name='Ключ задачи')
    name = models.CharField(max_length=512, verbose_name='Название')
    content = models.TextField(default='', blank=True, verbose_name='Содержимое')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
    due_date = models.DateField(blank=True, null=True, verbose_name='Дедлайн')
    reporter = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Репортер', related_name='reporter_issues')
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Создатель', related_name='creator_issues')
    assignee = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Исполнитель', related_name='assignee_issues')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def sync(server: Server):
        from .project import Project
        from .user import User
        jira = server.auth()
        users = User.objects.all()
        users_dict = {}
        for user in users:
            users_dict[user.user_key] = user
        for project in Project.objects.all():
            start_at = 0
            issues = jira.search_issues(f'project={project.project_key}', startAt=start_at)
            while len(issues) > 0:
                for issue in issues:
                    #
                    reporter = None
                    if issue.fields.reporter is not None and issue.fields.reporter.key in users_dict:
                        reporter = users_dict[issue.fields.reporter.key]
                    #
                    creator = None
                    if issue.fields.creator is not None and issue.fields.creator.key in users_dict:
                        creator = users_dict[issue.fields.creator.key]
                    #
                    assignee = None
                    if issue.fields.assignee is not None and issue.fields.assignee.key in users_dict:
                        assignee = users_dict[issue.fields.assignee.key]
                    #
                    issue_dict = {
                        'issue_key': issue.key,
                        'name': issue.fields.summary,
                        'content': issue.fields.description or "",
                        'project': project,
                        'reporter': reporter,
                        'creator': creator,
                        'assignee': assignee,
                        'created_at': issue.fields.created,
                        'due_date': issue.fields.duedate,
                    }
                    obj, created = Issue.objects.update_or_create(
                        issue_key=issue_dict['issue_key'],
                        defaults=issue_dict,
                    )
                time.sleep(1)
                start_at += 50
                issues = jira.search_issues(f'project={project.project_key}', startAt=start_at)
