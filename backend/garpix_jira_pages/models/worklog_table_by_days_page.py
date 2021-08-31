from garpix_page.models import BasePage
import datetime
from django.db.models import Sum


class WorklogTableByDaysPage(BasePage):
    template = 'garpix_jira/pages/worklog_table_by_days_page.html'

    def get_context(self, request=None, *args, **kwargs):
        from garpix_jira.models.worklog import WorkLog
        from garpix_jira.models.user import User as JiraUser
        context = super().get_context(request, *args, **kwargs)
        now = datetime.date.today()
        users = JiraUser.objects.filter(user_tracks_time=True).order_by('display_name')
        # data
        data = []
        dates = [now - datetime.timedelta(days=x) for x in range(14)]
        for user in users:
            data.append([
                user.display_name,
            ])
            for date in dates:
                seconds = WorkLog.objects.filter(
                    started_at__date=date,
                    author=user
                ).aggregate(summ=Sum('time_spent_seconds'))['summ']
                if seconds is None:
                    hours_float = 0
                else:
                    hours_float = float('{:.2f}'.format(seconds / 3600))
                # issues
                issues_keys = ', '.join(WorkLog.objects.filter(
                    started_at__date=date,
                    author=user
                ).select_related('issue').values_list('issue__issue_key', flat=True).distinct())
                data[len(data) - 1].append({
                    'value': hours_float,
                    'issues_keys': issues_keys,
                })

        context.update({
            'dates': dates,
            'data': data,
        })
        return context

    class Meta:
        verbose_name = "Jira - Затраченное время пользователей (страница)"
        verbose_name_plural = "Jira - Затраченное время пользователей (страница)"
        ordering = ('-created_at',)
