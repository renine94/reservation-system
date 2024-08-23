from rest_framework import status
from rest_framework.exceptions import APIException


class ReservationDuplicatedException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "이미 예약된 시험입니다."


class AlreadyConfirmedException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "이미 확정된 예약입니다."
