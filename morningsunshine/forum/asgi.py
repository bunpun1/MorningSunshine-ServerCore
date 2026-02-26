"""
ASGI config for forum project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

import os
from channels.routing import ProtocolTypeRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forum.settings')

application = django_asgi_app

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
})