from django.db import models
from .issue import Issue
from .user import User
from .server import Server


class WorkLog(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, verbose_name='Задача')
    time_spent_seconds = models.IntegerField(default=0, verbose_name='Затрекано времени')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
    started_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата/время записи журнала работ')
    worklog_key = models.CharField(max_length=50, verbose_name='Ключ журнала работ')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='author_worklogs')

    class Meta:
        verbose_name = 'Журнал работ'
        verbose_name_plural = 'Журналы работ'

    def __str__(self):
        return self.worklog_key

    @staticmethod
    def sync(server: Server):
        from .issue import Issue
        from .user import User
        from jira.exceptions import JIRAError
        jira = server.auth()
        users = User.objects.all()
        users_dict = {}
        for user in users:
            users_dict[user.user_key] = user
        for issue in Issue.objects.all():
            try:
                worklogs = jira.worklogs(issue.issue_key)
            except JIRAError:
                continue
            if worklogs is not None:
                for worklog in worklogs:
                    if worklog.author is not None and worklog.author.key in users_dict:
                        author = users_dict[worklog.author.key]
                        worklog_dict = {
                            'worklog_key': f'{worklog.issueId}__{worklog.id}',
                            'author': author,
                            'created_at': worklog.created,
                            'started_at': worklog.started,
                            'time_spent_seconds': worklog.timeSpentSeconds,
                            'issue': issue,
                        }
                        obj, created = WorkLog.objects.update_or_create(
                            worklog_key=worklog_dict['worklog_key'],
                            defaults=worklog_dict,
                        )
