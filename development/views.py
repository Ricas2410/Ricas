from django.shortcuts import render, get_object_or_404
from .models import DevelopmentService

def development_services(request):
    services = DevelopmentService.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'development/services.html', context)

def development_service_detail(request, slug):
    service = get_object_or_404(DevelopmentService, slug=slug)
    context = {
        'service': service,
    }
    return render(request, 'development/service_detail.html', context)
