from rest_framework import status
from rest_framework.exceptions import APIException


class ReservationDuplicatedException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "이미 예약된 시험입니다."


class AlreadyConfirmedException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "이미 확정된 예약입니다."


class InvalidReservationDateTimeException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "예약신청 가능 기간이 아닙니다."


class NotAllowedDeleteReservation(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "예약은 확정전에만 삭제가 가능합니다."


class NotAllowedUpdateReservation(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "예약은 확정전에만 수정이 가능합니다."
