from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .tasks import send_welcome_email   # ⬅️ Celery task

# ────────────────────────────────────────────────
#  PUBLIC ENDPOINT (no auth required)
# ────────────────────────────────────────────────
@api_view(["GET"])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public endpoint."})


# ────────────────────────────────────────────────
#  PROTECTED ENDPOINT (JWT or session auth)
# ────────────────────────────────────────────────
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response(
        {"message": f"Hello, {request.user.username}. You are authenticated!"}
    )


# ────────────────────────────────────────────────
#  USER REGISTRATION ENDPOINT
#  Triggers Celery welcome-email task
# ────────────────────────────────────────────────
@api_view(["POST"])
@permission_classes([AllowAny])  # Anyone can hit register
def register_user(request):
    """
    Expects JSON body:
    {
        "username": "...",
        "email":    "...",
        "password": "..."
    }
    """
    username = request.data.get("username")
    email    = request.data.get("email")
    password = request.data.get("password")

    # Basic validation
    if not all([username, email, password]):
        return Response(
            {"detail": "username, email and password are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if User.objects.filter(username=username).exists():
        return Response(
            {"detail": "Username already taken"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Create the user
    user = User.objects.create_user(username=username, email=email, password=password)

    # Kick off the background task
    send_welcome_email.delay(username, email)

    return Response(
        {
            "message": "User created. A welcome email is being sent in the background.",
            "user_id": user.id,
        },
        status=status.HTTP_201_CREATED,
    )
