### 1.7.0 (05.12.2021)

- Теперь есть возможность заполнять плановые эстимейты по документам (если это необходимо).

### 1.6.4 (04.12.2021)

- Исправлена ошибка с созданием категорий проектов.

### 1.6.1-1.6.3 (02.12.2021)

- Исправление небольших ошибок при импорте данных из Jira.

### 1.6.0 (02.12.2021)

- Добавлено больше полей для получения из Jira - `category`, `archived` для проекта; `resolution_date`, `resolution`, `time_estimate`, `time_spent`, `time_original_estimate` - для задачи.
- Убран модуль `garpix_jira_pages` ввиду его специфичности.

### 1.5.1 (26.11.2021)

- Ошибка с парсингом issues, когда нет проекта.

### 1.5.0 (23.11.2021)

- Добавлены специализации в таблицу трекинга пользователей.
- Добавлен фильтр по специализации в таблицу трекинга пользователей.
- Добавлен дополнительный фильтр по временному периоду в таблицу трекинга пользователей.

### 1.4.0-1.4.1 (16.11.2021)

- Дополнительные страницы.

### 1.2.1 (02.11.2021)

- Исправление ошибки с ID в контексте пейджа.

### 1.2.0 (02.11.2021)

- Переписан контекст пейджа (добавлен выбор периода и итого).
- Добавлен user_tracks_time в list_editable.

### 1.1.1 (02.09.2021)

- Исправлена ошибка с получением всех задач.

### 1.1.0 (20.08.2021)

- Исправлены ошибки
- Добавлен чекбокс "Пользователь трекает время?"
- Добавлен дополнительный пакет со списком страниц.
- Основной модуль `garpix_jira` отвязан от `garpixcms`.

### 1.0.0 (20.08.2021)

- Первый релиз на pypi.org.