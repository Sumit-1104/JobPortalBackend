from django.conf import settings
from django.db import models

from jobs.models import Job


class Application(models.Model):

    class Status(models.TextChoices):
      APPLIED = "APPLIED", "Applied"
      SHORTLISTED = "SHORTLISTED", "Shortlisted"
      HIRED = "HIRED", "Hired"
      REJECTED = "REJECTED", "Rejected"

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    resume = models.FileField(
        upload_to="resumes/"
    )

    cover_letter = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.APPLIED
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["job", "candidate"],
                name="unique_job_candidate_application"
            )
        ]

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"