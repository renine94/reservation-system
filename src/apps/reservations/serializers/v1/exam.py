from rest_framework import serializers

from src.apps.reservations.models.exam import Exam


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = [
            "id",
            "title",
            "description",
            "max_capacity",
            "current_capacity",
            "reservation_started_at",
            "reservation_ended_at",
            "started_at",
            "ended_at",
            "created_at",
        ]
        read_only_fields = ["current_capacity"]


class ExamReservationCreateSerializer(serializers.Serializer):
    number_of_applicants = serializers.IntegerField(min_value=1, help_text="응시 인원 수")
