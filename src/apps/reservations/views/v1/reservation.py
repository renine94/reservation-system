from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from src.apps.reservations.models import Reservation
from src.apps.reservations.serializers.v1 import ReservationSerializer
from src.apps.reservations.services.v1 import ReservationService
from src.core.enums.reservation import ReservationStatusEnum
from src.core.errors.reservation import NotAllowedUpdateReservation
from src.core.permissions import IsAdminOnly
from src.core.permissions import IsOwnerOnly


class ReservationAPI(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """관리자는 모든 예약을 가져오고, 고객은 본인의 예약목록만 조회가능"""
        user = self.request.user
        queryset = super().get_queryset()
        return queryset if user.is_staff else queryset.filter(user=user)


class ReservationDetailAPI(viewsets.GenericViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsOwnerOnly,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if request.user.is_staff or instance.status != ReservationStatusEnum.CONFIRM.value:
            super().perform_update(serializer)
        else:
            raise NotAllowedUpdateReservation

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_destroy(self, instance: Reservation):
        ReservationService.remove_reservation(self.request.user, instance)

    @action(methods=["post"], detail=True, permission_classes=[IsAdminOnly])
    def confirm(self, request, pk):
        """예약 확정"""
        reservation: Reservation = self.get_object()
        reservation.confirm()
        reservation.refresh_from_db()
        serializer = self.get_serializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)
