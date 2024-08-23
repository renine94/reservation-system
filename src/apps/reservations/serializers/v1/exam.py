from rest_framework import serializers

from src.apps.reservations.models.exam import Exam


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = [
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
