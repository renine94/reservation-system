from rest_framework import serializers

from src.apps.reservations.models import Reservation
from src.apps.reservations.serializers.v1 import ExamSerializer


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    exam = ExamSerializer()

    class Meta:
        model = Reservation
        fields = ["id", "user", "exam", "status", "number_of_applicants", "created_at", "updated_at"]
        read_only_fields = []
