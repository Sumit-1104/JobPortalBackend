from django.urls import path
from .views import (
    JobListCreateView,
    JobDetailView,
    EmployerDashboardView,
    EmployerMyJobsView,
)

urlpatterns = [
    path(
    "employer-dashboard/",
    EmployerDashboardView.as_view(),
    name="employer-dashboard-api"
    ),

    path(
    "my-jobs/",
    EmployerMyJobsView.as_view(),
    name="employer-my-jobs"
    ),
    
    path("", JobListCreateView.as_view(), name="job-list-create"),
    path("<int:pk>/", JobDetailView.as_view(), name="job-detail"),
]