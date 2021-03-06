Запуск проекта
==============

Для начала необходимо установить [vagga](http://vagga.readthedocs.io/en/latest/installation.html#ubuntu) (из репозитория *testing*)

Требуется версия не ниже **v0.8.0** (проверить можно через `vagga --version`)

В этой версии том `mysql` инициализируется и заполняется данными автоматически, включая применение миграций, так что при удалении его из `.vagga/.volumes/mysql` и последующем запуске проекта он корректно инициализирутся.

Затем нужно собрать статику:

    vagga build-static

Запустить проект

    vagga run

Другое
======

* cправка по отдельным командам — `vagga` без аргументов
* данные `!Persistent` томов доступны в `.vagga/.volumes/`
* логи PHP — `.vagga/.volumes/php_log`, рекомендуется `tail -f .vagga/.volumes/php_log/tabun.error.log` в другой консоли для просмотра ошибок
* загруженные файлы — `.vagga/.volumes/storage`
* время от времени можно чистить неиспользуемые образы — `vagga _clean --unused`

Локальные сервисы
=================

Redis
-----
Порт `6379`

*Базы:*

* 1 — брокер Celery
* 2 — результаты задач
* 3 — сессии PHP
* 4 — кеш приложения

MySQL
-----
Порт `3306`

php-fpm
-------
Порт `1818`
Порт xDebug `39000` (ключ *tabun*)

Почта
-----

При запуске дерева процессов также запускается отладочный почтовый сервер, позволяющий тестировать связанный с отправкой писем функционал.
Интерфейс для чтения локальных писем расположен по адресу http://127.0.0.1:1080/

База данных
-----------

Для загрузки SQL-дампов либо выполнения любых других корректных комманд, в т.ч. сжатые (`*.sql.gz`) существует комманда `_load_fixture`

При использовании команды **требуется остановить проект**, если он запущен с помощь `vagga run`. Если процессы запущены по отдельности, например, `vagga run --only php`, `vagga run --only mysql` и т.д., то нужно остановить только процесс `mysql`

Например, загрузка сжатого дампа будет выглядеть примерно так:

    vagga _load_fixture my/test/dump.sql.gz

Либо, применение патча:

    vagga _load_fixture my/patches/31337_info.sql

Фикстуры
--------

При заполнении базы данных для тестирования доступно четыре аккаунта:

    Celestia:celestia
    Luna:constellations
    Sparkle:scrolls
    Spitfire:feathers
