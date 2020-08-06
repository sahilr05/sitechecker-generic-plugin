from celery import shared_task
from checkerapp.models import AlertPlugin
from django.db import models


class GenericAlertPlugin(AlertPlugin):
    url = "accounts:generic_plugin:generic_pluginview"
    user_id = models.CharField(max_length=50)

    @shared_task
    def send_alert_task(task_obj):
        return "Generic task"
