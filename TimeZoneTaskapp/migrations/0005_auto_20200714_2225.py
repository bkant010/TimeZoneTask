# Generated by Django 2.2.8 on 2020-07-14 16:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TimeZoneTaskapp', '0004_auto_20200714_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task_type',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='task_time',
            unique_together={('user', 'task_type', 'country', 'start_time', 'end_time')},
        ),
    ]
