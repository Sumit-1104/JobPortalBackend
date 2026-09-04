import json

from django.contrib.auth import get_user_model
from django.test import Client, TestCase


User = get_user_model()


class AuthFlowTests(TestCase):
    def setUp(self):
        self.client = Client(HTTP_HOST="testserver")

    def test_signup_and_login_work_with_testserver_host(self):
        payload = {
            "username": "candidateuser",
            "email": "candidate@example.com",
            "password": "SecurePass123",
            "role": "CANDIDATE",
        }

        signup_response = self.client.post(
            "/api/auth/signup/",
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(signup_response.status_code, 201)
        self.assertTrue(User.objects.filter(username="candidateuser").exists())

        token_response = self.client.post(
            "/api/token/",
            data=json.dumps({
                "username": "candidateuser",
                "password": "SecurePass123",
            }),
            content_type="application/json",
        )

        self.assertEqual(token_response.status_code, 200)
        self.assertIn("access", token_response.json())
        self.assertIn("refresh", token_response.json())
