from django.shortcuts import render, get_object_or_404
from .models import CybersecurityService, CybersecurityTestimonial
from settings.models import BannerImage

def cybersecurity_services(request):
    """View for listing all cybersecurity services"""
    services = CybersecurityService.objects.all()
    testimonials = CybersecurityTestimonial.objects.filter(is_featured=True)

    # Get banner images
    banners = {}
    for banner in BannerImage.objects.all():
        banners[banner.section] = banner

    context = {
        'services': services,
        'testimonials': testimonials,
        'banners': banners,
    }

    return render(request, 'cybersecurity/services.html', context)

def cybersecurity_service_detail(request, slug):
    """View for a single cybersecurity service"""
    service = get_object_or_404(CybersecurityService, slug=slug)
    related_services = CybersecurityService.objects.exclude(id=service.id)[:3]

    # Get banner images
    banners = {}
    for banner in BannerImage.objects.all():
        banners[banner.section] = banner

    context = {
        'service': service,
        'related_services': related_services,
        'banners': banners,
    }

    return render(request, 'cybersecurity/service_detail.html', context)
