from celery import shared_task
from django.core.mail import send_mail
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(username, email):
    subject = "Welcome to the Platform"
    message = f"Hi {username}, thank you for registering!"
    from_email = "noreply@example.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

@shared_task
def send_welcome_email(username, email):
    send_mail(
        subject="Welcome to the Platform",
        message=f"Hi {username}, thank you for registering!",
        from_email="noreply@example.com",
        recipient_list=[email],
    )
