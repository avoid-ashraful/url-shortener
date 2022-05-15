from django.urls import path

from links.views import LinkCreateAPIView

app_name = "links"


urlpatterns = [path("", LinkCreateAPIView.as_view(), name="create")]
