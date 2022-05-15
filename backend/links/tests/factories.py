from factory import django

from links.models import Link
from links.utils import FuzzyUrl


class LinkFactory(django.DjangoModelFactory):
    url_address = FuzzyUrl()

    class Meta:
        model = Link
