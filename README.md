# Garpix Jira

Интеграция с Jira Server. Является частью GarpixCMS.

## Быстрый старт

Установка через pipenv:

```bash
pipenv install garpix_jira
```

Добавьте `garpix_jira` в `INSTALLED_APPS` и укажите адрес для миграций:

```python
# settings.py
from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'garpix_jira',
]

MIGRATION_MODULES['garpix_jira'] = 'app.migrations.garpix_jira'
```

Создайте директории и файлы:

```bash
backend/app/migrations/garpix_jira/
backend/app/migrations/garpix_jira/__init__.py
```

Сделайте миграции и мигрируйте:

```bash
python3 backend/manage.py makemigrations
python3 backend/manage.py migrate
```

После этого необходимо создать адрес сервера, с которым будем интегрироваться и ввести учетные данные администратора Jira [http://localhost:8000/admin/garpix_jira/server/](http://localhost:8000/admin/garpix_jira/server/)

Теперь, можно забрать данные из Jira в ваш проект. Для этого выполните команду (она будет периодически запускать данные):

```bash
python3 backend/manage.py jira_sync_all
```

# Changelog

See [CHANGELOG.md](CHANGELOG.md).

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

# License

[MIT](LICENSE)

---

Developed by Garpix / [https://garpix.com](https://garpix.com)