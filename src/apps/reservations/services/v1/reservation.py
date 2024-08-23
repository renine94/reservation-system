from django.db import IntegrityError

from src.apps.accounts.models import User
from src.apps.reservations.models import Exam
from src.apps.reservations.models import Reservation
from src.core.enums.reservation import ReservationStatusEnum
from src.core.errors.reservation import InvalidReservationDateTimeException
from src.core.errors.reservation import NotAllowedDeleteReservation
from src.core.errors.reservation import ReservationDuplicatedException


class ReservationService:

    @classmethod
    def reserve_exam(cls, user: User, exam: Exam):
        """
        시험 예약
        1. 예약은 시험 시작 3일 전까지 신청가능
        """
        if not exam.is_reservable:
            raise InvalidReservationDateTimeException

        try:
            reservation = Reservation.objects.create(user_id=user.id, exam_id=exam.id)
        except IntegrityError:
            raise ReservationDuplicatedException
        return reservation

    @classmethod
    def remove_reservation(cls, user: User, reservation: Reservation):
        """
        1. 운영자는 예약 삭제 가능
        2. 고객은 예약이 확정 상태가 아닐 때만, 삭제가능
        """
        if user.is_staff or reservation.status != ReservationStatusEnum.CONFIRM.value:
            reservation.delete()
        else:
            raise NotAllowedDeleteReservation

