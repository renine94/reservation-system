from src.core.base.enum import BaseEnum


class ReservationStatusEnum(BaseEnum):
    """
    예약에 쓰이는 상태값 관리
    """

    PENDING = "PENDING"  # 대기
    CANCELED = "CANCELED"  # 취소
    CONFIRM = "CONFIRM"  # 확정
