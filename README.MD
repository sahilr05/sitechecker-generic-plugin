# SiteChecker Generic bot

Generic plugin for Site Checker

## How to install

Find python package in dist, download and install it.
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
