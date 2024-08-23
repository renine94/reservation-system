from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from src.apps.reservations.models.exam import Exam
from src.apps.reservations.serializers.v1 import ExamSerializer
from src.apps.reservations.services.v1 import ReservationService


class ExamAPI(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return super().get_queryset()

    @action(methods=["post"], detail=False)
    def reservation(self, request, pk):
        """시험을 예약하고, 예약상태를 PENDING 으로 초기화"""
        exam = get_object_or_404(self.queryset, pk=pk)
        reservation = ReservationService.reserve_exam(request.user, exam)
        return Response(reservation, status=status.HTTP_200_OK)
