from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from src.apps.reservations.models import Reservation
from src.apps.reservations.serializers.v1 import ReservationSerializer
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

    @action(methods=["post"], detail=True)
    def confirm(self, request, pk):
        reservation: Reservation = self.get_object()
        reservation.confirm()
        serializer = self.get_serializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)
