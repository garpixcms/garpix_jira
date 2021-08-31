from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'garpix_jira',
    'garpix_jira_pages',
]

MIGRATION_MODULES['garpix_jira'] = 'app.migrations.garpix_jira'
MIGRATION_MODULES['garpix_jira_pages'] = 'app.migrations.garpix_jira_pages'
