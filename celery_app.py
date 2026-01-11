from celery import Celery
import os

broker = os.getenv("CELERY_BROKER", "redis://redis:6379/0")
celery = Celery("payments", broker=broker)
celery.conf.task_routes = {"app.tasks.*": {"queue": "payments"}}
celery.conf.result_backend = os.getenv("CELERY_RESULT_BACKEND", broker)
