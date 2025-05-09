"""
Test script to verify email functionality.
Run this script with: python test_email.py
"""

import os
import sys
import django
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ricas_it_services.settings')
django.setup()

def test_email():
    """Send a test email to verify SMTP configuration."""
    print("Testing email functionality...")
    
    # Get email settings from environment
    email_host = os.environ.get('EMAIL_HOST', '')
    email_port = os.environ.get('EMAIL_PORT', '')
    email_user = os.environ.get('EMAIL_HOST_USER', '')
    email_password = os.environ.get('EMAIL_HOST_PASSWORD', '')
    
    # Check if email settings are configured
    if not email_user or not email_password:
        print("\nWARNING: Email settings not fully configured.")
        print("Make sure to set the following environment variables:")
        print("  - EMAIL_HOST (currently: {})".format(email_host or 'not set'))
        print("  - EMAIL_PORT (currently: {})".format(email_port or 'not set'))
        print("  - EMAIL_HOST_USER (currently: {})".format(email_user or 'not set'))
        print("  - EMAIL_HOST_PASSWORD (currently: {})".format('*****' if email_password else 'not set'))
        print("\nEmail will be sent to the console instead of actual recipients.")
    
    # Prepare test data
    context = {
        'name': 'Test User',
        'email': 'test@example.com',
        'subject': 'Test Subject',
        'message': 'This is a test message to verify email functionality.',
        'phone': '1234567890',
        'site_name': getattr(settings, 'SITE_NAME', 'Ricas IT Services'),
        'site_url': getattr(settings, 'SITE_URL', 'https://ricasitservices.com'),
    }
    
    # Render email templates
    email_subject = f"Test Email: {context['subject']}"
    email_message = render_to_string('contact/email/notification.txt', context)
    html_message = render_to_string('contact/email/notification.html', context)
    
    # Get recipient email (use admin email or default to sender)
    admin_email = os.environ.get('ADMIN_EMAIL', email_user)
    
    try:
        # Send email
        send_mail(
            subject=email_subject,
            message=email_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[admin_email or 'test@example.com'],
            html_message=html_message,
            fail_silently=False,
        )
        print("\nTest email sent successfully!")
        print(f"Check the inbox of: {admin_email or 'console output'}")
        
        # Also test the confirmation email
        user_subject = f"Thank you for contacting {context['site_name']}"
        user_message = render_to_string('contact/email/confirmation.txt', context)
        user_html_message = render_to_string('contact/email/confirmation.html', context)
        
        send_mail(
            subject=user_subject,
            message=user_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[admin_email or 'test@example.com'],
            html_message=user_html_message,
            fail_silently=False,
        )
        print("Confirmation email sent successfully!")
        
    except Exception as e:
        print(f"\nError sending email: {e}")
        print("\nPlease check your email configuration in the .env file.")
        return False
    
    return True

if __name__ == "__main__":
    success = test_email()
    sys.exit(0 if success else 1)
