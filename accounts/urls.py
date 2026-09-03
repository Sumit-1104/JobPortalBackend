from django.urls import path
from .views import SignupView, ProfileView, CandidateDetailView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),

    path("profile/", ProfileView.as_view(), name="profile"),
    
    path(
    "candidate/<int:candidate_id>/",
    CandidateDetailView.as_view(),
    name="candidate-detail",
    ),
]