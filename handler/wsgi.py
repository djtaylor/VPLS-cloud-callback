import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vm_callback.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
