from django.urls import path

from ..views import v1

app_name = "reservations-v1"

# fmt: off
urlpatterns = [
    # Exam
    path("exams/", lambda x: x, name="exam-list"),

    # Reservation
    path("reservations/", lambda x: x, name="reservation-list"),

]
