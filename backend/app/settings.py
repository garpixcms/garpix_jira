from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'garpix_jira',
    'debug_toolbar',
]

MIGRATION_MODULES['garpix_jira'] = 'app.migrations.garpix_jira'  # noqa

MIDDLEWARE += [  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]
