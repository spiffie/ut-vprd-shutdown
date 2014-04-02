Shutdown: _A Django App To Shut Down Your Django App_
=====

This is a simple app that can be used to bring down a PyPE django project by
simply adding an entry to an oracle table.

Usage
=====

To include this app in your PyPE project, simply pull it into your project via svn:externals.

> path: extra/shutdown

> URL: https://github.com/UT-Austin-FIS/shutdown/tags/1.2/shutdown

Setup
------

1. Add "shutdown" to your INSTALLED_APPS setting like this::

```python
      INSTALLED_APPS = (
          ...
          'shutdown',
      )
```

2. Add the shutdown middleware to your MIDDLEWARE_CLASSES setting like this::

```python
      MIDDLEWARE_CLASSES= (
          ...
          'shutdown.middleware.ShutdownMiddleware',
      )
```

3. Add an SHUTDOWN_CONTEXT object to your settings.py. This should be a class that carries the core of your page context logic. If not supplied, the UTDirectContext will be used, but you will need to supply the api key in your settings (eg: API_KEY = 'your_api_key')::

```python
   SHUTDOWN_CONTEXT = 'path.to.your.desired.context.object'
```

4. Add an SHUTDOWN_DEFAULT_REDIRECT to your settings.py. This should be the name url pattern, and will be used to redirect any users attempting to access the shutdown urls directly, when there is no outage occuring.::

```python
   SHUTDOWN_DEFAULT_REDIRECT = 'url_name' # e.g.: 'home'
```

5. Include the shutdown URLconf in your project urls.py like this::

```python
    url(r'^apps/services/requests/', include(shutdown.urls)),
```

6. Run `python manage.py syncdb` to create the shutdown models.


**NOTE**: 
_Since this app creates a new table, if your database design involves multiple users, you will need to go through the same process that you typically use to migrate a table and grant privileges._
