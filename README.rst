==================================================================
Django Zinibu SEO
==================================================================

Django application used by the zinibu project, based on django-zinibu-skeleton.

The application provides:

* The basics for creating a reusable Django application with setuptools that can be installed from the Python Package Index (PyPI) via pip.


Logging
--------------------------------------------------

There's `a bug <https://github.com/docker/for-mac/issues/307>`_ that causes Docker not to follow the logs making it difficult to see console output and debug using Django's development server or Gunicorn from the Django application. To work around this use Django's logging system. Start by adding this to your settings file:

.. code-block:: bash

  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'formatters': {
          'verbose': {
              'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
          },
      },
      'handlers': {
          'console': {
              'level': 'INFO',
              'class': 'logging.FileHandler',
              'filename': '/var/log/debug.log',
              'formatter': 'verbose'
          },
      },
      'loggers': {
          '': {
              'handlers': ['console'],
              'level': 'INFO',
          }
      },
  }
  
And then you can add logging calls in the appropiate parts of your code. I'm adding pretty printing here:

.. code-block:: bash

  import logging
  import pprint
  logger = logging.getLogger(__name__)
  logger.info(pprint.pformat(vars(object)))
 

See `Django logging documentation <https://docs.djangoproject.com/en/1.11/topics/logging/>`_ for details.

