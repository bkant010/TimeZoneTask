# Generated by Django 2.2.8 on 2020-07-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeZoneTaskapp', '0008_auto_20200715_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_day',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_day',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set(),
        ),
    ]
