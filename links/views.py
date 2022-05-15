from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from links.models import Link
from links.serializers import LinkSerializer


class BaseLink:
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [AllowAny]


class LinkCreateAPIView(BaseLink, CreateAPIView):
    def create(self, request, *args, **kwargs):
        url_address = request.POST.get("url_address", "")
        link = Link.objects.filter(url_address=url_address)
        if not link.exists():
            return super(LinkCreateAPIView, self).create(request, *args, **kwargs)

        serializer = self.get_serializer(link.last())
        return Response(serializer.data, status=status.HTTP_409_CONFLICT)


class LinkRetrieveAPIView(BaseLink, RetrieveAPIView):
    lookup_field = "key"
