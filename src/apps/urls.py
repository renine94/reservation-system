from django.urls import include
from django.urls import path


urlpatterns = [
    path("v1/", include("src.apps.accounts.urls.v1")),
]
