import random
import string
from functools import lru_cache

from django.core.exceptions import ValidationError
from factory.fuzzy import FuzzyText


class FuzzyUrl(FuzzyText):
    def __init__(
        self,
        prefix="https://www.",
        suffix=".com",
        length=100,
        chars=string.ascii_letters,
    ):
        super().__init__()
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.chars = tuple(chars)  # Unroll iterators


@lru_cache(maxsize=128)
def get_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


@lru_cache(maxsize=128)
def get_nPr(n, r):
    return get_factorial(n)/get_factorial(n-r)


def get_key_length(total_links):
    for i in range(4, 255):
        k = get_nPr(62, i)

        if (k * 0.8) > total_links:  # avoiding 20%, for less probability of duplication
            return i + 1


def get_unique_key():
    from links.models import Link
    from links.urls import app_name

    links = Link.objects.all()

    key_length = get_key_length(links.count() + 1)
    attempts = 0
    while attempts < 5:
        key = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(key_length)
        )
        if not links.filter(key=key).exists() and key != app_name:
            return key
        attempts += 1

    # if not successful in creating unique key for 5 iterations
    raise ValidationError(
        {
            "key": [
                "Can not produce unique key.",
            ]
        }
    )
