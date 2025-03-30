Запуск:
    1 python3 -m venv venv
    2 source venv/bin/activate
    3 pip install -r requirements.txt
    4 python3 manage.py makemigrations
    5 python3 manage.py migrate
    6 python populate_db.py (генерация фейковых данных)
    7 python3 manage.py createsuperuser
    8 python3 manage.py runserver

Структура:

    Фильтрация: Доступна по полям, указанным в filterset_fields

    Поиск: Работает по полям из search_fields

    Пагинация: 10 элементов на страницу

    Доступ: Только для чтения неавторизованным пользователям

    Slug вместо ID: Для проектов и блога используется поле slug в URL

    -------------------------------------------------------------------

    CRUD операции для всех моделей

    Фильтрациея и поиск

    Пагинация

    Поддержка изображений

    Опциональная аутентификация


Urls тестирование

    /api/developers/ - список разработчиков

    /api/projects/<slug>/ - конкретный проект

    /api/blog/?tag=django - посты с определенным тегом