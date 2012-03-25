import sys
sys.path.append('/home/chunwei/')

from django.core.management import setup_environ
import swin.settings as settings
setup_environ(settings)

from swin.reptile.models import Author

a = Author(name="superjom", content="hello world")
a.save()
