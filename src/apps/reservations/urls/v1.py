from django.urls import path

from ..views import v1

app_name = "reservations-v1"

# fmt: off
urlpatterns = [
    # Exam
    path("exams/", v1.ExamAPI.as_view({"get": "list", "post": "create"}), name="exam-list"),
    path("exams/<int:pk>/", v1.ExamAPI.as_view({"get": "retrieve", "delete": "destroy", "put": "update"}), name="exam-detail"),
    path("exams/<int:pk>/reservation/", v1.ExamAPI.as_view({"post": "reservation"}), name="exam-reservation"),

    # Reservation
    path("reservations/", v1.ReservationAPI.as_view(), name="reservation-list"),
    path("reservations/<int:pk>/", v1.ReservationDetailAPI.as_view({"get": "retrieve", "delete": "destroy", "put": "update"}), name="reservation-detail"),
    path("reservations/<int:pk>/confirm/", v1.ReservationDetailAPI.as_view({"post": "confirm"}), name="reservation-confirm"),

]
