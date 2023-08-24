from django.db.models.signals import post_save
from .models import Task, Reminder
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone



@receiver(post_save, sender=Task)
def create_reminder(sender, instance, created, **kwargs):
    if created and instance.deadline:
        reminder_time = instance.deadline - timedelta(minutes=20) #send reminder 20mins before the deadline
        if reminder_time > timezone.now():
            Reminder.objects.create(
                user=instance.user,
                task=instance,
                reminder_time=reminder_time
            )