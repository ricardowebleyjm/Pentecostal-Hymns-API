"""
URL configuration for pentecostal_hymns_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from ninja import NinjaAPI

from hymns.api import router as hymns_router



api = NinjaAPI(
    title="Pentecostal Hymns API",
    version="1.0.0",
    description="Contains a collection of all Pentecostal Hymns",
)
api.add_router("/hymns/", hymns_router)


def index_view(request: HttpRequest):
    return HttpResponse(content="<h1>Penecostal Hymns API</h1>")

urlpatterns = [
    path("", index_view, "index_view"),
    path('admin/', admin.site.urls),
    path("api/v1/", api.urls),
]


