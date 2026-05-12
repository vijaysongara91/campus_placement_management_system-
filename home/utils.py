from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_shortlist_email(student_email, student_name):
    html_content = render_to_string('email/shortlist.html', {'name': student_name})
    email = EmailMultiAlternatives(
        subject="Placement Shortlisting Notification",
        body="You are shortlisted for the interview.",
        from_email=settings.EMAIL_HOST_USER,
        to=[student_email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
