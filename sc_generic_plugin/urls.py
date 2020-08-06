from django.urls import path

from sc_generic_plugin import views

app_name = "sc_generic_plugin"

urlpatterns = [path("", views.PluginView, name="generic_pluginview")]
