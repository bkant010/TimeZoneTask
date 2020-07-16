from django.db import models
class Task(models.Model):
    user = models.CharField(max_length=50)
    task_type=models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    start_time=models.TimeField()
    end_time = models.TimeField()
    start_day = models.CharField(max_length=50)
    end_day = models.CharField(max_length=50)
