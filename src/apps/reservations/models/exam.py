from django.db import models
from django.utils import timezone

from src.core.base.model import BaseModel
from src.core.errors.exam import NotEnoughCapacityException, MaxCapacityExceededException


class ExamManager(models.Manager):
    pass


class ExamQuerySet(models.QuerySet):
    pass


class Exam(BaseModel):
    """
    시험 테이블
    나중에 기능이 확장설계되면, 하나의 회사가 여러개의 시험을 가질 수 있게 되고, company 필드가 추가될듯?
    """

    users = models.ManyToManyField("accounts.User", related_name="exams", through="reservations.Reservation")
    title = models.CharField("시험 제목", max_length=255)
    description = models.TextField("시험 내용")
    max_capacity = models.PositiveIntegerField("최대 시험 응시 가능 고객수", default=50000)
    current_capacity = models.PositiveIntegerField("현재 시험 신청 고객수", default=0)  # 예약 확정해야 계산
    reservation_started_at = models.DateTimeField("예약 시작 시간")
    reservation_ended_at = models.DateTimeField("예약 종료 시간")
    started_at = models.DateTimeField("시험 시작 시간")
    ended_at = models.DateTimeField("시험 종료 시간")

    objects = ExamManager.from_queryset(ExamQuerySet)()

    class Meta:
        verbose_name_plural = verbose_name = "시험"
        ordering = ["-pk"]
        indexes = [
            models.Index(fields=["title"], name="idx_title"),
        ]

    def __str__(self):
        return self.title

    @property
    def has_capacity(self):
        """
        시험 예약 할 수 있는지 체크
        1. 시험에 예약은 N개 있으나, 예약확정이 되어야만 current_capacity 값을 업데이트해줍니다.
        """
        return self.max_capacity > self.current_capacity

    @property
    def is_reservable(self) -> bool:
        """
        시험은 3일전까지 예약 가능
        """
        return (self.started_at - timezone.now()) <= timezone.timedelta(days=3)

    def increase_current_capacity(self, value: int = 1):
        """
        현재 응시생 수를 증가시킵니다.
        """

        # 시험 응시인원이 꽉찼을 때,
        if not self.has_capacity:
            raise NotEnoughCapacityException

        # 증가하고자 하는 응시인원이 수용가능한 상태를 초과할 때,
        if self.current_capacity + value > self.max_capacity:
            raise MaxCapacityExceededException

        self.current_capacity += value
        self.save(update_fields=["current_capacity"])
