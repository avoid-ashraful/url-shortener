import pytest
from django.urls import reverse
from rest_framework import status
from factory.fuzzy import FuzzyText

from links.models import Link
from links.tests.factories import LinkFactory
from links.utils import FuzzyUrl


class TestLinkBase:
    link_size = 1000

    @pytest.fixture()
    def links(
        self,
    ):
        return LinkFactory.create_batch(size=self.link_size)

    @pytest.fixture()
    def random_url(self):
        return FuzzyUrl(length=10).fuzz()


class TestLinkCreateViews(TestLinkBase):
    @pytest.fixture
    def url(self):
        return reverse(
            "api:links:create",
        )

    def test_link_creation(self, client, random_url, url):
        data = {"url_address": random_url}
        response = client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get("url_address") == data.get("url_address")
        assert (
            response.data.get("key")
            == Link.objects.get(url_address=response.data.get("url_address")).key
        )

    def test_duplicate_link_creation(self, client, random_url, url, links):

        data = {"url_address": links[0].url_address}
        response = client.post(url, data)

        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.data.get("url_address") == data.get("url_address")
        assert (
            response.data.get("key")
            == Link.objects.get(url_address=response.data.get("url_address")).key
        )

    def test_invalid_link_creation(self, client, random_url, url, links):

        data = {"url_address": FuzzyText().fuzz()}
        response = client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestLinkRetrieveViews(TestLinkBase):
    @pytest.fixture
    def url(self, links):
        return reverse("link-retrieve", args=[links[0].key])

    def test_link_retrieve(self, client, random_url, url, links):

        data = {"key": links[0].key}
        response = client.get(url, data=data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("url_address") == links[0].url_address
        assert response.data.get("key") == links[0].key
