import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings")

from faker import Faker
from lost.models import Lost
from django.contrib.auth.models import User
from django.utils import timezone

