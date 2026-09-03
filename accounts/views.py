# Create your views here.

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import SignupSerializer, ProfileSerializer, CandidateDetailSerializer

class SignupView(APIView):

    def get(self, request):
        return render(request, "accounts/signup.html")

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "User registered successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = ProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request):
        return self.put(request)

class CandidateDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, candidate_id):

        # Only employers can view candidate details
        if request.user.role != "EMPLOYER":
            return Response(
                {
                    "detail": "Only employers can view candidate details."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            candidate = User.objects.get(
                id=candidate_id,
                role="CANDIDATE"
            )
        except User.DoesNotExist:
            return Response(
                {
                    "detail": "Candidate not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CandidateDetailSerializer(candidate)

        return Response(serializer.data)