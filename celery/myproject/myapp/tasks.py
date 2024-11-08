from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(user_email):
    subject = 'Welcome to My Site!'
    message = 'Thanks for signing up to our service.'
    from_email = settings.DEFAULT_FROM_EMAIL

    # Send the email asynchronously
    send_mail(subject, message, from_email, [user_email])

    print(f"Welcome email sent to {user_email}")
    return f"Welcome email sent to {user_email}"