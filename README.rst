
URL-Shortener: URL shortening service in python

=====================================================

A application for a very simple URL shortening service

The application relies on:

- flask_: A python micro web framework
- bootstrap_: A CSS & JS framework
- redis_: A Redis in-memory-db

The URL-Shortener Application can be accessible using:

http://<LISTEN_HOST:LISTEN_PORT>

eg. http://127.0.0.1:5000

Installing
----------

Redis:

1) download and install redis

URL-Shortener:

1) pip install virtualenv
2) virtualenv flask
3) /flask/Scripts/activate
4) python setup.py install
5) pip install url_shortener
6) go to /url_shortener/ directory
7) python __init__.py 


Configuration
-------------

You can either modify the ``config.py`` file or provide environment variables to configure ``url_shortener``.
The following environment variables can be tweaked:

- ``REDIS_HOST``: Address at which the redis server lives, defaults to ``127.0.0.1``.
- ``REDIS_PORT``: Port on which to contact redis, defaults to ``6379``.
- ``URL_PREFIX``: URL scheme for your short url host
- ``LISTEN_HOST``: Address to bind to for the short url service
- ``LISTEN_PORT``: Port to bind to
- ``RIEMANN_HOST``: Address to use to contact riemann, defaults to ``127.0.0.1``
- ``RIEMANN_PORT``: Port to use to contact riemann, defaults to ``5555``
- ``LOG_FILE_PATH``: Where to log, no defaults
- ``LOG_LEVEL``: level at which to log, defaults to ``DEBUG``

Logging
-------

When not run in debug mode, the application will output logs for consumption by using logstash_formatter

