# SiteChecker Generic bot

Generic plugin template for Site Checker <br/>
Checkout [Sitechecker Telegram plugin](https://github.com/sahilr05/sitechecker-telegram-plugin)

## Creating custom plugin
* Go to ```models.py``` and replace ```generic``` with your plugin name wherever mentioned. <br/>
Eg. ```url = "accounts:telegram_plugin:telegram_pluginview"``` <br/>
  Configure ```def send_alert_task(task_obj)```
* Go to ```forms.py, views.py, urls.py, admin.py ``` and replace ```generic``` with your plugin name



## How to install

* Run 
```
python setup.py sdist
```
Find python package in dist and run
```
pip install sc_generic_plugin.tar.gz
```

## Integrating in SiteChecker

* Add sc_generic_plugin in settings > INSTALLED_APPS

```
INSTALLED_APPS = [
...
...
"sc_generic_plugin",
]
```

* Add following url in sitechecker > accounts > urls.py

```
path("plugin/generic_plugin",include("sc_generic_plugin.urls", namespace="generic_plugin")),
```
* Run migrations
