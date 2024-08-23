from django.db import IntegrityError

from src.apps.reservations.models import Reservation
from src.core.enums.reservation import ReservationStatusEnum
from src.core.errors.reservation import ReservationDuplicatedException


class ReservationService:

    @classmethod
    def reserve_exam(cls, user_id: int, exam_id: int):
        """
        시험 예약
        """
        try:
            reservation = Reservation.objects.create(user_id=user_id, exam_id=exam_id)
        except IntegrityError:
            raise ReservationDuplicatedException
        return reservation
