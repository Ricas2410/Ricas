from django.shortcuts import render, get_object_or_404
from .models import EducationService

def education_services(request):
    services = EducationService.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'education/services.html', context)

def education_service_detail(request, slug):
    service = get_object_or_404(EducationService, slug=slug)
    context = {
        'service': service,
    }
    return render(request, 'education/service_detail.html', context)
