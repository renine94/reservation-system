from rest_framework import status
from rest_framework.exceptions import APIException


class NotEnoughCapacityException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "시험 신청 가능 인원이 마감되었습니다."


class MaxCapacityExceededException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "시험 신청 가능 인원을 초과합니다."
