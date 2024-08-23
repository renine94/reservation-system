from django.db import IntegrityError

from src.apps.accounts.models import User
from src.apps.reservations.models import Reservation, Exam
from src.core.errors.reservation import ReservationDuplicatedException, ReservationTooEarlyException


class ReservationService:

    @classmethod
    def reserve_exam(cls, user: User, exam: Exam):
        """
        시험 예약
        1. 예약은 시험 시작 3일 전까지 신청가능
        """
        if not exam.is_reservable:
            raise ReservationTooEarlyException

        try:
            reservation = Reservation.objects.create(user_id=user.id, exam_id=exam.id)
        except IntegrityError:
            raise ReservationDuplicatedException
        return reservation
