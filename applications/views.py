from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

from .models import Application
from .serializers import ApplicationSerializer


class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        if request.user.role != "CANDIDATE":
            raise PermissionDenied(
                "Only candidates can apply for jobs."
            )

        job_id = request.data.get("job")

        already_applied = Application.objects.filter(
            job_id=job_id,
            candidate=request.user
        ).exists()

        if already_applied:
            return Response(
                {
                    "detail": "You have already applied for this job."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(candidate=request.user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


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

class EmployerApplicationStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != "EMPLOYER":
            raise PermissionDenied(
                "Only employers can update application status."
            )

        return Application.objects.filter(
            job__employer=self.request.user
        )

    def update(self, request, *args, **kwargs):

        application = self.get_object()

        new_status = request.data.get("status")

        allowed_statuses = [
        "APPLIED",
        "SHORTLISTED",
        "REJECTED",
        "HIRED",
        ]

        if new_status not in allowed_statuses:
            return Response(
                {
                    "detail": (
                        "Invalid status. Choose "
                        "APPLIED, SHORTLISTED, "
                        "HIRED or REJECTED."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        application.status = new_status
        application.save(update_fields=["status"])

        serializer = self.get_serializer(application)

        return Response(serializer.data)


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


from jobs.models import Job


class EmployerDashboardView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "EMPLOYER":
            raise PermissionDenied(
                "Only employers can access the dashboard."
            )

        employer_jobs = Job.objects.filter(employer=request.user)
        total_jobs = employer_jobs.count()
        active_jobs = total_jobs

        employer_applications = Application.objects.filter(
            job__employer=request.user
        ).order_by("-applied_at")

        total_applications = employer_applications.count()
        recent_applications = employer_applications[:5]
        serializer = ApplicationSerializer(recent_applications, many=True)

        return Response({
            "total_jobs": total_jobs,
            "total_applications": total_applications,
            "active_jobs": active_jobs,
            "recent_applications": serializer.data,
        })
