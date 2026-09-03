# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        CANDIDATE = "CANDIDATE", "Candidate"
        EMPLOYER = "EMPLOYER", "Employer"

    role = models.CharField(
        max_length=20,
        choices=Role.choices
    )

    # Candidate Profile
    full_name = models.CharField(
        max_length=150,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    skills = models.TextField(
        blank=True
    )

    experience = models.TextField(
        blank=True
    )

    education = models.TextField(
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    resume = models.FileField(
    upload_to="resumes/",
    blank=True,
    null=True
    )

    def __str__(self):
        return f"{self.username} - {self.role}"