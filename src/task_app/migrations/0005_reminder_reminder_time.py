# Generated by Django 4.2.4 on 2023-08-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_app", "0004_category_user_tag_user_reminder"),
    ]

    operations = [
        migrations.AddField(
            model_name="reminder",
            name="reminder_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
