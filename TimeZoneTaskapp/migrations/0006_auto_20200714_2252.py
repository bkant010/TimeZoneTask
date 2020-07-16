# Generated by Django 2.2.8 on 2020-07-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeZoneTaskapp', '0005_auto_20200714_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_time',
            name='end_day',
            field=models.CharField(choices=[('None', 'None'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='task_time',
            name='start_day',
            field=models.CharField(choices=[('None', 'None'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='task_time',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='task_time',
            name='start_time',
            field=models.TimeField(),
        ),
    ]