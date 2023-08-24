from django.utils import timezone
from .models import Reminder
from datetime import timedelta
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from celery import shared_task
import subprocess


logger = get_task_logger(__name__)


@shared_task()
def send_task_reminder():
    now = timezone.now()
    near_reminders = Reminder.objects.filter(reminder_time__gte=now, reminder_time__lte=now + timedelta(minutes=15), notified=False)
    
    for reminder in near_reminders:
        # Send a reminder notification
        send_mail(
            'Reminder',
            f"Your reminder for '{reminder.task}' is due soon.",
            'noreply@example.com',
            [reminder.user.email],
            fail_silently=False,
        )
        
        reminder.notified = True
        reminder.save()


@shared_task
def run_backup_script():
    subprocess.run(["python", "backup_script.py"])