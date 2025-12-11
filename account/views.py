from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

class TestApiView(APIView):

    @extend_schema(
        summary="Test API endpoint",
        description="Returns a simple hello message",
        responses={200: dict}
    )
    def get(self, request):
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)





@csrf_exempt
def github_update_webhook(request):
    # Only allow POST
    if request.method != "POST":
        return HttpResponseForbidden("Invalid method")

    # Check secret token
    received_token = request.headers.get("X-GITHUB-TOKEN")
    expected_token = getattr(settings, "GITHUB_WEBHOOK_SECRET", None)

    if not expected_token or received_token != expected_token:
        return HttpResponseForbidden("Invalid or missing token")

    # Log for debugging (optional)
    print("GitHub webhook received:", request.body)

    return JsonResponse({"message": "received successfuly"})