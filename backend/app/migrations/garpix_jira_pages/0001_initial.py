# Generated by Django 3.1 on 2021-08-31 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorklogTableByDaysPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Jira - Затраченное время пользователей (страница)',
                'verbose_name_plural': 'Jira - Затраченное время пользователей (страница)',
                'ordering': ('-created_at',),
            },
            bases=('garpix_page.basepage',),
        ),
    ]