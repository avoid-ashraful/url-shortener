import random
import string
from functools import reduce, lru_cache
import operator as op

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
def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer / denom


def check_r(total_links):
    for i in range(4, 255):
        k = ncr(62, i)

        if (k * 0.8) > total_links:  # avoiding 20%, for less probability of duplication
            return i + 1


def get_unique_key():
    from links.models import Link
    from links.urls import app_name

    links = Link.objects.all()

    url_length = check_r(links.count() + 1)
    attempts = 0
    while attempts < 5:
        key = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(url_length)
        )
        if not links.filter(key=key).exists() and key != app_name:
            return key

    # if not successful in creating unique key for 5 iterations
    raise ValidationError(
        {
            "key": [
                "Can not produce unique key.",
            ]
        }
    )
