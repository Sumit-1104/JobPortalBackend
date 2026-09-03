from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied

from .models import Job
from .serializers import JobSerializer
from applications.models import Application
from rest_framework.response import Response


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]

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

        serializer.save(
            employer=self.request.user
        )


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]

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

class EmployerDashboardView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "EMPLOYER":
            raise PermissionDenied(
                "Only employers can access the dashboard."
            )

        # Employer jobs
        employer_jobs = Job.objects.filter(
            employer=request.user
        )

        total_jobs = employer_jobs.count()

        # Currently all posted jobs are active
        active_jobs = employer_jobs.count()

        # Employer applications
        employer_applications = Application.objects.filter(
            job__employer=request.user
        )

        total_applications = employer_applications.count()

        # Status counts
        pending_applications = employer_applications.filter(
            status="APPLIED"
        ).count()

        shortlisted_applications = employer_applications.filter(
            status="SHORTLISTED"
        ).count()

        hired_applications = employer_applications.filter(
            status="HIRED"
        ).count()

        rejected_applications = employer_applications.filter(
            status="REJECTED"
        ).count()

        # Recent applications
        recent_applications = employer_applications.order_by(
            "-applied_at"
        )[:5]

        recent_data = []

        for application in recent_applications:

            recent_data.append({
                "id": application.id,
                "job_title": application.job.title,
                "company": application.job.company,
                "candidate": application.candidate.username,
                "candidate_email": application.candidate.email,
                "status": application.status,
                "applied_at": application.applied_at,
            })

        return Response({
            "total_jobs": total_jobs,
            "active_jobs": active_jobs,
            "total_applications": total_applications,

            "pending_applications": pending_applications,
            "shortlisted_applications": shortlisted_applications,
            "hired_applications": hired_applications,
            "rejected_applications": rejected_applications,

            "recent_applications": recent_data,
        })

class EmployerMyJobsView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.user.role != "EMPLOYER":
            raise PermissionDenied(
                "Only employers can view their jobs."
            )

        return Job.objects.filter(
            employer=self.request.user
        ).order_by("-created_at")