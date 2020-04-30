import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceshi.settings')

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, BASE_DIR)
django.setup()

from app.models import User
user = User()
