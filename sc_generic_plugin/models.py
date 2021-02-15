from celery import shared_task
from checkerapp.models import AlertPlugin
from checkerapp.models import AlertSent
from django.db import models
from django.db.models import Q

from .plugin import send_alert


class GenericAlertPlugin(AlertPlugin):
    url = "accounts:generic_plugin:generic_pluginview"
    user_id = models.CharField(max_length=50)

    @shared_task
    def send_alert_task(task_obj):
        check_obj = task_obj["base_check_obj"]
        message = str(check_obj.content_object) + " is down"
        users = list(check_obj.service_set.first().users.all())

        for user in users:
            generic_user_obj = GenericAlertPlugin.objects.filter(
                Q(alert_receiver=user) & Q(active_status=True)
            ).first()
            if not generic_user_obj:
                print("Inactive")
                break
            send_alert(message, generic_user_obj)
            AlertSent.objects.create(check_obj=check_obj)
            return "Success !"
