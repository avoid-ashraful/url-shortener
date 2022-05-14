import random
import string
from functools import reduce
import operator as op

from links.models import Link


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer / denom


def check_r(total_links):
    for i in range(2, 255):
        k = ncr(62, i)

        # if k > total_links:
        if (k / total_links) > 0.9:
            return i + 1


def random_string():
    total_links = Link.objects.all()

    url_length = check_r(total_links)
    return "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(url_length)
    )
