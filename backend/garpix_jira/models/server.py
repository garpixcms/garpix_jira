from django.db import models
from jira import JIRA
import logging


class Server(models.Model):
    login = models.CharField(max_length=150, verbose_name='Логин')
    password = models.CharField(max_length=150, verbose_name='Пароль')
    server = models.CharField(max_length=200, default='https://jira.atlassian.com', verbose_name='Сервер jira')

    def __str__(self):
        return self.server

    class Meta:
        verbose_name = 'Сервер Jira'
        verbose_name_plural = 'Серверы Jira'
        ordering = ('server',)

    def auth(self):
        jira = JIRA(server=self.server, basic_auth=(self.login, self.password))
        return jira

    @classmethod
    def sync_all(cls):
        from .project import Project
        from .user import User
        from .issue import Issue
        from .worklog import WorkLog
        from django.utils import timezone
        #
        for server in cls.objects.all():
            print(f"Start at {timezone.now()}")
            User.sync(server)
            print(f"{timezone.now()} - Users imported")
            Project.sync(server)
            print(f"{timezone.now()} - Projects imported")
            Issue.sync(server)
            print(f"{timezone.now()} - Issues imported")
            WorkLog.sync(server)
            print(f"{timezone.now()} - WorkLogs imported")
