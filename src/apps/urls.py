from django.urls import include
from django.urls import path


urlpatterns = [
    # v1
    path("v1/", include("src.apps.accounts.urls.v1")),
    path("v1/", include("src.apps.reservations.urls.v1")),

    # v2 (TBD)
]
