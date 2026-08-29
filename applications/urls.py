from django.urls import path

from .views import (
    ApplicationCreateView,
    EmployerApplicationListView,
    CandidateApplicationListView,
)

urlpatterns = [
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