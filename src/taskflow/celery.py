import os
from datetime import timedelta
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskflow.settings")
app = Celery("taskflow")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Add this to schedule the check_deadlines task
app.conf.beat_schedule = {
    'check-deadlines': {
        'task': 'task_app.tasks.send_task_reminder',  # Replace with your actual app and task name
        'schedule': timedelta(minutes=1),  # Set the interval (e.g., run every 5 minutes)
    },
    'run-backup-script': {
        'task': 'task_app.tasks.run_backup_script',  # Replace with your actual app and task name
        'schedule': crontab(hour=2, minute=0),  # Schedule to run daily at 2:00 AM
    },
}