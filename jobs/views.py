from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Job
from .serializers import JobSerializer


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Job.objects.all().order_by("-created_at")

        search = self.request.query_params.get("search")
        location = self.request.query_params.get("location")
        job_type = self.request.query_params.get("job_type")

        if search:
            queryset = queryset.filter(
                title__icontains=search
            )

        if location:
            queryset = queryset.filter(
                location__icontains=location
            )

        if job_type:
            queryset = queryset.filter(
                job_type=job_type
            )

        return queryset

    def perform_create(self, serializer):
        if self.request.user.role != "EMPLOYER":
            raise PermissionDenied(
                "Only employers can create jobs."
            )

        serializer.save(employer=self.request.user)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user.role != "EMPLOYER":
            raise PermissionDenied(
                "Only employers can update jobs."
            )

        if serializer.instance.employer != self.request.user:
            raise PermissionDenied(
                "You can only update your own jobs."
            )

        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role != "EMPLOYER":
            raise PermissionDenied(
                "Only employers can delete jobs."
            )

        if instance.employer != self.request.user:
            raise PermissionDenied(
                "You can only delete your own jobs."
            )

        instance.delete()