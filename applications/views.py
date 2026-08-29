from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Application
from .serializers import ApplicationSerializer


class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "CANDIDATE":
            raise PermissionDenied(
                "Only candidates can apply for jobs."
            )

        serializer.save(candidate=self.request.user)


class EmployerApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != "EMPLOYER":
            raise PermissionDenied(
                "Only employers can view applications."
            )

        return Application.objects.filter(
            job__employer=self.request.user
        ).order_by("-applied_at")

class CandidateApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != "CANDIDATE":
            raise PermissionDenied(
                "Only candidates can view their applications."
            )

        return Application.objects.filter(
            candidate=self.request.user
        ).order_by("-applied_at")