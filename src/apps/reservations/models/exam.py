from django.db import models

from src.core.base.model import BaseModel


class ExamManager(models.Manager):
    pass


class ExamQuerySet(models.QuerySet):
    pass


class Exam(BaseModel):
    """
    시험 테이블
    나중에 기능이 확장설계되면, 하나의 회사가 여러개의 시험을 가질 수 있게 되고, company 필드가 추가될듯?
    """
    title = models.CharField("시험 제목", max_length=255)
    description = models.TextField("시험 내용")
    max_capacity = models.PositiveIntegerField("최대 시험 응시 가능 고객수", default=50000)
    current_capacity = models.PositiveIntegerField("현재 시험 신청 고객수", default=0)  # 예약 확정해야 계산
    reservation_started_at = models.DateTimeField("예약 시작 시간")
    reservation_ended_at = models.DateTimeField("예약 종료 시간")
    started_at = models.DateTimeField("시험 시작 시간")
    ended_at = models.DateTimeField("시험 종료 시간")

    objects = ExamManager.from_queryset(ExamQuerySet)()

    def __str__(self):
        return self.title
