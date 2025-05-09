from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
from settings.models import SiteSettings

def contact(request):
    # Get site settings for email configuration
    site_settings = SiteSettings.objects.first()
    admin_email = getattr(settings, 'ADMIN_EMAIL', None)

    if site_settings and site_settings.email:
        admin_email = site_settings.email

    # Get service type from query parameters
    service_type = request.GET.get('service_type', '')
    product = request.GET.get('product', '')

    initial_data = {}
    if service_type:
        subject_prefix = {
            'education': 'ICT Education Inquiry',
            'development': 'Software Development Inquiry',
            'cybersecurity': 'Cybersecurity Services Inquiry',
            'network': 'Network Services Inquiry',
        }.get(service_type, '')

        if subject_prefix:
            initial_data['subject'] = subject_prefix

    if product:
        initial_data['subject'] = f"Product Inquiry: {product}"

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save()

            # Send email notification
            try:
                # Prepare email content
                context = {
                    'name': contact_message.name,
                    'email': contact_message.email,
                    'subject': contact_message.subject,
                    'message': contact_message.message,
                    'phone': contact_message.phone,
                    'site_name': getattr(settings, 'SITE_NAME', 'Ricas IT Services'),
                    'site_url': getattr(settings, 'SITE_URL', 'https://ricasitservices.com'),
                }

                # Render email templates
                email_subject = f"New Contact Form Submission: {contact_message.subject}"
                email_message = render_to_string('contact/email/notification.txt', context)
                html_message = render_to_string('contact/email/notification.html', context)

                # Send email
                if admin_email:
                    send_mail(
                        subject=email_subject,
                        message=email_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[admin_email],
                        html_message=html_message,
                        fail_silently=False,
                    )

                    # Send confirmation email to the user
                    user_subject = f"Thank you for contacting {getattr(settings, 'SITE_NAME', 'Ricas IT Services')}"
                    user_message = render_to_string('contact/email/confirmation.txt', context)
                    user_html_message = render_to_string('contact/email/confirmation.html', context)

                    send_mail(
                        subject=user_subject,
                        message=user_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[contact_message.email],
                        html_message=user_html_message,
                        fail_silently=False,
                    )
            except Exception as e:
                # Log the error but don't show it to the user
                print(f"Error sending email: {e}")

            messages.success(request, 'Your message has been sent. We will get back to you soon!')
            return redirect('contact')
    else:
        form = ContactForm(initial=initial_data)

    context = {
        'form': form,
        'service_type': service_type,
        'product': product,
    }
    return render(request, 'contact/contact.html', context)
