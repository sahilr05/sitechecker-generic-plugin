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
        user_id = form.cleaned_data.get("user_id")
        GenericAlertPlugin.objects.create(
            user_id=user_id, alert_receiver=request.user
        )  # NOQA

    context = {"form": form, "plugin_name": GenericAlertPlugin.__name__}
    return render(request, "plugins/plugin.html", context)
