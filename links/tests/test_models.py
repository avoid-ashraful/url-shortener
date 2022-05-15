from links.models import Link
from links.tests.factories import LinkFactory


def unique_key_checker(iteration=10000):

    links = LinkFactory.create_batch(size=iteration)
    assert len(links) == iteration


def test_unique_key_generation():
    for i in range(10):
        unique_key_checker()
        print(f"{Link.objects.count()} links created in test database")
