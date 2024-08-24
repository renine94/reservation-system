from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from src.apps.reservations.models.exam import Exam
from src.apps.reservations.serializers.v1 import ExamSerializer, ReservationSerializer
from src.apps.reservations.serializers.v1.exam import ExamReservationCreateSerializer
from src.apps.reservations.services.v1 import ReservationService


class ExamAPI(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'reservation':
            return ExamReservationCreateSerializer
        return super().get_serializer_class()

    @action(methods=["post"], detail=False, serializer_class=ExamReservationCreateSerializer)
    def reservation(self, request, pk):
        """시험을 예약하고, 예약상태를 PENDING 으로 초기화"""
        serializer: ExamReservationCreateSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        exam = get_object_or_404(self.queryset, pk=pk)
        reservation = ReservationService.reserve_exam(request.user, exam, **validated_data)
        return Response(ReservationSerializer(reservation).data, status=status.HTTP_200_OK)
