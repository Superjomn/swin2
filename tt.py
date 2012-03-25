from django.core.management import setup_environ
import settings

setup_environ(settings)

from reptile.models import Author

a = Author(name="superjom", content="hello world")
a.save()
