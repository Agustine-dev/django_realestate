import sys, os

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "realestate.settings" # change 'application_name' to
                                                                   # the name of the Django project

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

