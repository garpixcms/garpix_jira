from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'garpix_jira',
]

MIGRATION_MODULES['garpix_jira'] = 'app.migrations.garpix_jira'
