from django.db import models
from garpix_page.models import BasePage
import datetime
from django.db.models import Sum
import pandas


class SpecializationWorklogTableByDaysPage(BasePage):
    template = "garpix_jira/pages/specialization_worklog_table_by_days.html"

    def get_context(self, request=None, *args, **kwargs):
        from garpix_jira.models.worklog import WorkLog
        context = super().get_context(request, *args, **kwargs)
        # filters
        now = datetime.date.today()

        year = int(request.GET.get('year', now.year))
        context['year'] = year

        month = int(request.GET.get('month', now.month))
        context['month'] = month

        alltime = int(request.GET.get('alltime', 0)) == 1
        context['alltime'] = alltime

        if alltime:
            data = WorkLog.objects.select_related('issue', 'author').all()
        else:
            data = WorkLog.objects.select_related('issue', 'author').filter(
                started_at__year=year,
                started_at__month=month,
            )
        data = data.values('issue__project__name', 'author__specialization_id'). \
            annotate(summ=Sum('time_spent_seconds', output_field=models.FloatField()) / 3600.0). \
            values('issue__project__name', 'author__specialization__title', 'summ')
        df = pandas.DataFrame(data)
        records = list(df.to_records(index=False))
        records.insert(0, ['Проект', 'Специальность', 'Часы'])
        context['data'] = records
        return context

    class Meta:
        verbose_name = "Jira - Затраченное время специалистов по проектам (страница)"
        verbose_name_plural = "Jira - Затраченное время специалистов по проектам (страница)"
        ordering = ('-created_at',)
