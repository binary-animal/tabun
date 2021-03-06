BROKER_URL = 'redis://127.0.0.1:6579/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6579/2'
CELERY_IMPORTS = ("tasks",)

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_ENABLE_UTC = True
