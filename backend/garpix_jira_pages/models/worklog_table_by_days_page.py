from garpix_page.models import BasePage
import datetime
from django.db import connection


SQL_GET_WORKLOGS = '''
SELECT day_date, garpix_jira_user.display_name as display_name, author_id, sum_time_spent_seconds, garpix_jira_specialization.title as spec
FROM (SELECT day_date, author_id, SUM(time_spent_seconds) as sum_time_spent_seconds
      FROM (SELECT generate_series(%s, %s, '1 day'::interval)::date as day_date) as dates
      JOIN garpix_jira_worklog ON date(garpix_jira_worklog.started_at) = dates.day_date
      GROUP BY author_id, day_date
) worklogs
JOIN garpix_jira_user ON garpix_jira_user.id = worklogs.author_id
LEFT JOIN garpix_jira_specialization ON garpix_jira_user.specialization_id = garpix_jira_specialization.id
'''


class WorklogTableByDaysPage(BasePage):
    template = 'garpix_jira/pages/worklog_table_by_days_page.html'

    def get_context(self, request=None, *args, **kwargs):
        from garpix_jira.models.user import User as JiraUser
        from garpix_jira.models.specialization import Specialization
        context = super().get_context(request, *args, **kwargs)
        # filter_specialization_id
        try:
            filter_specialization_id = int(request.GET.get('filter_specialization_id', None))
        except:
            filter_specialization_id = None
        # dates filter
        FILTER_DATES_LAST_WEEK = 1
        FILTER_DATES_CUSTOM = 2
        FILTER_DATES_CURRENT_MONTH = 3
        FILTER_DATES_PREV_MONTH = 4
        try:
            filter_dates = int(request.GET.get('filter_dates', FILTER_DATES_LAST_WEEK))
        except:
            filter_dates = FILTER_DATES_LAST_WEEK
        # dates
        if filter_dates == FILTER_DATES_LAST_WEEK:
            date_to = datetime.date.today()
            date_from = date_to - datetime.timedelta(days=7)
        elif filter_dates == FILTER_DATES_CUSTOM:
            date_to_str = request.GET.get('to')
            if date_to_str is not None:
                date_to = datetime.datetime.strptime(date_to_str, '%Y-%m-%d').date()
            else:
                date_to = datetime.date.today()
            date_from_str = request.GET.get('from')
            if date_from_str is not None:
                date_from = datetime.datetime.strptime(date_from_str, '%Y-%m-%d').date()
            else:
                date_from = date_to - datetime.timedelta(days=40)
        elif filter_dates == FILTER_DATES_CURRENT_MONTH:
            date_to = datetime.date.today()
            date_from = date_to.replace(day=1)
        elif filter_dates == FILTER_DATES_PREV_MONTH:
            date_to = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
            date_from = date_to.replace(day=1)
        # days_between = 40
        delta = date_to - date_from
        dates = [date_to - datetime.timedelta(days=x) for x in range(delta.days + 1)]
        # users
        users = JiraUser.objects.select_related('specialization').filter(user_tracks_time=True)
        if filter_specialization_id is not None:
            users = users.filter(specialization_id=filter_specialization_id)
        users = users.order_by('display_name').values('display_name', 'id', 'specialization__title')
        specializations = Specialization.objects.all()
        # data
        data = []
        with connection.cursor() as cursor:
            sql = SQL_GET_WORKLOGS
            if filter_specialization_id is not None:
                sql += f' WHERE garpix_jira_specialization.id = {filter_specialization_id};'
            else:
                sql += ';'
            cursor.execute(sql, [date_from, date_to])
            rows = cursor.fetchall()
            #
            d = {}
            for item in rows:
                day_date = item[0]
                display_name = item[1]
                user_id = item[2]
                value = item[3]
                spec = item[4]
                if user_id not in d:
                    d[user_id] = {}
                d[user_id][day_date] = value
            for user in users:
                data.append([user['display_name']])
                if user['specialization__title'] is not None:
                    data[-1].append(user['specialization__title'])
                else:
                    data[-1].append('')
                total = 0
                for date in dates:
                    day_date_is_weekend = date.weekday() > 4
                    if user['id'] in d and date in d[user['id']]:
                        hours_float = float('{:.2f}'.format(d[user['id']][date] / 3600))
                        total += hours_float
                        data[-1].append({
                            'value': hours_float,
                            'issues_keys': '',
                            'is_weekend': day_date_is_weekend,
                        })
                    else:
                        data[-1].append({
                            'value': 0,
                            'issues_keys': '',
                            'is_weekend': day_date_is_weekend,
                        })
                data[-1].insert(2, total)
        context.update({
            'dates': dates,
            'data': data,
            'date_to': date_to,
            'date_from': date_from,
            'filter_specialization_id': filter_specialization_id,
            'specializations': specializations,
            'filter_dates': filter_dates,
        })
        return context

    class Meta:
        verbose_name = "Jira - Затраченное время пользователей (страница)"
        verbose_name_plural = "Jira - Затраченное время пользователей (страница)"
        ordering = ('-created_at',)
