from django.urls import path

from .views import (
    ApplicationCreateView,
    EmployerApplicationListView,
    CandidateApplicationListView,
    EmployerDashboardView,
    EmployerApplicationStatusUpdateView,
)

urlpatterns = [
    path(
    "employer/dashboard/",
    EmployerDashboardView.as_view(),
    name="employer-dashboard"
    ),  

    path(
    "<int:pk>/status/",
    EmployerApplicationStatusUpdateView.as_view(),
    name="employer-application-status-update"
    ),

    path(
        "",
        ApplicationCreateView.as_view(),
        name="application-create"
    ),
    path(
        "employer/",
        EmployerApplicationListView.as_view(),
        name="employer-applications"
    ),

    path(
    "my-applications/",
    CandidateApplicationListView.as_view(),
    name="my-applications"
    ),
]