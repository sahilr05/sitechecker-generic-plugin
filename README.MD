# SiteChecker Generic bot

Generic plugin template for Site Checker <br/>
Checkout [Sitechecker Telegram plugin](https://github.com/sahilr05/sitechecker-telegram-plugin)

## Creating custom plugin
* Replace ```generic``` with your plugin name wherever mentioned. <br/>
  Eg. ```url = "accounts:telegram_plugin:telegram_pluginview"``` <br/>

* Configure ```send_alert``` function in ```plugin.py```

## How to install

* Run following command to create package
```
python setup.py sdist
```
* Find python package in dist and run
```
pip install sc_generic_plugin.tar.gz
```

## Integrating with SiteChecker

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
