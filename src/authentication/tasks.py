from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_otp_email_task(email, otp):
    send_mail(
        subject="Your OTP Code",
        message=f"Your OTP is {otp}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )


@shared_task
def send_password_reset_email_task(email, reset_link):
    send_mail(
        subject="Reset your password",
        message=f"Click the link below to reset your password:\n\n{reset_link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )