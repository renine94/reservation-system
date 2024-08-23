from django.db import models, transaction

from src.core.base.model import BaseModel
from src.core.enums.reservation import ReservationStatusEnum
from src.core.errors.reservation import AlreadyConfirmedException
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.apps.reservations.models import Exam


class ReservationManager(models.Manager):
    pass


class ReservationQuerySet(models.QuerySet):
    pass


class Reservation(BaseModel):
    """
    예약 테이블
    """

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="reservations")
    exam = models.ForeignKey("reservations.Exam", on_delete=models.CASCADE, related_name="reservations")
    status = models.CharField(
        "예약 상태", max_length=10, choices=ReservationStatusEnum.items(), default=ReservationStatusEnum.PENDING.value
    )

    objects = ReservationManager.from_queryset(ReservationQuerySet)()

    class Meta:
        verbose_name_plural = verbose_name = "예약"
        ordering = ["-pk"]
        indexes = [
            models.Index(fields=["user", "exam"], name="idx_user_exam"),
            models.Index(fields=["status"], name="idx_status"),
        ]
        constraints = [models.UniqueConstraint(fields=["user", "exam"], name="unique_user_exam")]

    def __str__(self):
        return f"{self.user}'s reservation for {self.exam}"

    @transaction.atomic
    def confirm(self):
        """
        예약확정
        1. 예약확정시, Exam의 현재 예약한 인원을 갱신해줘야 합니다.
        2. 예약확정이, 동시에 이루어질 가능성을 염두하여, select_for_update() 를 사용하여 경쟁상태를 방지합니다.
        """
        if self.status == ReservationStatusEnum.CONFIRM.value:
            raise AlreadyConfirmedException

        self.status = ReservationStatusEnum.CONFIRM.value
        self.save(update_fields=["status"])

        exam: "Exam" = self.exam.__class__.objects.select_for_update().get(pk=self.exam.pk)
        exam.increase_current_capacity()

        return self
