<<<<<<< HEAD
"""
WSGI config for huudeey project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huudeey.settings")

application = get_wsgi_application()
=======
"""
WSGI config for huudeey project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huudeey.settings")

application = get_wsgi_application()
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
