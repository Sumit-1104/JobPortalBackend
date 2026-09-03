"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
# from django.http import JsonResponse
from django.shortcuts import render
from accounts.views import SignupView
from django.http import FileResponse

def home(request):
    return render(request, "home.html")

def resume_view(request, path):
    file_path = settings.MEDIA_ROOT / path

    if not file_path.exists():
        from django.http import Http404
        raise Http404("Resume not found")

    response = FileResponse(
        open(file_path, "rb"),
        content_type="application/pdf"
    )

    response["Content-Disposition"] = "inline"

    return response

def login_page(request):
    return render(request, "login.html")

def jobs_page(request):
    return render(request, "jobs.html")

def job_detail_page(request, pk):
    return render(request, "job_detail.html")

def my_applications_page(request):
    return render(request, "my_applications.html")

def employer_applications_page(request):
    return render(request, "employer_applications.html")

def employer_dashboard_page(request):
    return render(request, "employer_dashboard.html")

def employer_post_job_page(request):
    return render(request, "employer_post_job.html")

def employer_my_jobs_page(request):
    return render(request, "employer_my_jobs.html")

def employer_edit_job_page(request, pk):
    return render(request, "employer_edit_job.html")

def employer_view_job_page(request, pk):
    return render(request, "employer_view_job.html")

def employer_profile_page(request):
    return render(request, "employer_profile.html")

def employer_candidate_page(request, candidate_id):
    return render(
        request,
        "employer_candidate.html",
        {
            "candidate_id": candidate_id
        }
    )

def candidate_profile_page(request):
    return render(
        request,
        "candidate_profile.html"
    )

def candidate_profile_view_page(request):
    return render(
        request,
        "candidate_profile_view.html"
    )

urlpatterns = [
    path("", home),

    path("login/", login_page),

    path("jobs/", jobs_page),

    path("jobs/<int:pk>/", job_detail_page, name="job-detail-page"),

    path(
    "my-applications/",
    my_applications_page,
    name="my-applications-page"
    ),

    path(
    "employer-applications/",
    employer_applications_page,
    name="employer-applications-page"
    ),

    path(
    "employer-dashboard/",
    employer_dashboard_page,
    name="employer-dashboard-page"
    ),

    path(
    "employer-post-job/",
    employer_post_job_page,
    name="employer-post-job-page"
    ),

    path(
    "employer-my-jobs/",
    employer_my_jobs_page,
    name="employer-my-jobs-page"
    ),

    path(
    "employer-edit-job/<int:pk>/",
    employer_edit_job_page,
    name="employer-edit-job-page"
    ),

    path(
    "employer-view-job/<int:pk>/",
    employer_view_job_page,
    name="employer-view-job-page"
    ),

    path(
    "employer-profile/",
    employer_profile_page,
    name="employer-profile-page"
    ),

    path(
    "employer-candidate/<int:candidate_id>/",
    employer_candidate_page,
    name="employer-candidate-page"
    ),

    path(
    "candidate-profile/",
    candidate_profile_page,
    name="candidate-profile-page"
    ),

    path(
    "candidate-profile-view/",
    candidate_profile_view_page,
    name="candidate-profile-view-page"
    ),

    path(
    "resume-view/<path:path>/",
    resume_view,
    name="resume-view"
    ),

    path("signup/", SignupView.as_view(), name="signup"),

    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),

    path("api/jobs/", include("jobs.urls")),

    path(
    "api/applications/",
    include("applications.urls")
    ),

    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )