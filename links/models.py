from django.core.validators import URLValidator
from django.db import models

from links.utils import get_unique_key


class Link(models.Model):

    url_address = models.URLField(unique=True, validators=[URLValidator])
    key = models.CharField(unique=True, default=get_unique_key, max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["url_address", "key"], name="url_with_key"),
        ]

    def __str__(self):
        return f"{self.url_address}, {self.key}, {self.created_at}"

    def __repr__(self):
        return self.__str__()
