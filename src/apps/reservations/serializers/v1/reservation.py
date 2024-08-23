from rest_framework import serializers

from src.apps.reservations.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    exam = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = [
            "id",
            "user",
            "exam",
            "status",
            "created_at",
            "updated_at"
        ]
        read_only_fields = []
