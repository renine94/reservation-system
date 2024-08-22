from django.db import models

from src.core.base.model import BaseModel
from src.core.enums.reservation import ReservationStatusEnum


class ReservationManager(models.Manager):
    pass


class ReservationQuerySet(models.QuerySet):
    pass


class Reservation(BaseModel):
    """
    예약 테이블
    """
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='reservations')
    exam = models.ForeignKey("Exam", on_delete=models.CASCADE, related_name='reservations')
    status = models.CharField("예약 상태", max_length=10, choices=ReservationStatusEnum.items())

    objects = ReservationManager.from_queryset(ReservationQuerySet)()

    def __str__(self):
        return f"{self.user}'s reservation for {self.exam}"
