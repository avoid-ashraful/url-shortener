from django.core.validators import URLValidator
from django.db import models

from links.utils import random_string


class Link(models.Model):

    url_address = models.URLField(unique=True, validators=[URLValidator])
    key = models.CharField(unique=True, default=random_string, max_length=255)
    created_at = models.DateTimeField(auto_now=True)
