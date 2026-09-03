from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(
        source="employer.username",
        read_only=True
    )

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "company",
            "location",
            "salary",
            "description",
            "requirements",
            "job_type",
            "employer",
            "employer_name",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "employer",
            "employer_name",
            "created_at",
        ]
