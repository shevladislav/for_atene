import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
django.setup()

from bookstore.models import PaperBook

print(PaperBook)
