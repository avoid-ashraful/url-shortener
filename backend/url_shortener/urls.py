"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from links.urls import app_name
from links.views import LinkRetrieveAPIView

api_patterns = [
    path(f"{app_name}/", include("links.urls", namespace="link")),
]


urlpatterns = [
    path(
        "api/",
        include(arg=(api_patterns, "url_shortener"), namespace="api"),
    ),
    path(
        "<str:key>/",
        LinkRetrieveAPIView.as_view(),
        name="link-retrieve",
    ),
]