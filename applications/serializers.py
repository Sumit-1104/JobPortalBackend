from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    candidate_name = serializers.CharField(
        source="candidate.username",
        read_only=True
    )

    job_title = serializers.CharField(
        source="job.title",
        read_only=True
    )

    class Meta:
        model = Application
        fields = [
            "id",
            "job",
            "job_title",
            "candidate",
            "candidate_name",
            "resume",
            "cover_letter",
            "status",
            "applied_at",
        ]

        read_only_fields = [
            "id",
            "candidate",
            "candidate_name",
            "job_title",
            "status",
            "applied_at",
        ]