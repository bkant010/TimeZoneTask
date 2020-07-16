from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['user','task_type', 'country','start_time','end_time','start_day','end_day']

admin.site.register(Task,TaskAdmin)