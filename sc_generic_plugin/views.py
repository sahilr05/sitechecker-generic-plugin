from django.shortcuts import render

from .forms import GenericAlertForm
from .models import GenericAlertPlugin


def PluginView(request):
    user = request.user
    try:
        generic_obj = GenericAlertPlugin.objects.get(alert_receiver=user.pk)
    except Exception:
        generic_obj = None

    form = GenericAlertForm(request.POST or None, instance=generic_obj)

    if request.method == "POST" and form.is_valid():
        try:
            old_user_id = (
                GenericAlertPlugin.objects.filter(alert_receiver=user.pk)
                .first()
                .user_id
            )
            new_user_id = form.cleaned_data.get("user_id")
            active_status = form.cleaned_data.get("active_status")
            GenericAlertPlugin.objects.filter(user_id=old_user_id).update(  # NOQA
                user_id=new_user_id, active_status=active_status
            )
        except Exception:
            user_id = form.cleaned_data.get("user_id")
            active_status = form.cleaned_data.get("active_status")
            GenericAlertPlugin.objects.create(
                user_id=user_id,
                alert_receiver=request.user,
                active_status=active_status,
            )

    context = {"form": form, "plugin_name": GenericAlertPlugin.__name__}
    return render(request, "plugins/plugin.html", context)
