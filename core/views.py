from django.shortcuts import render
from .models import TeamMember, Testimonial
from education.models import EducationService
from development.models import DevelopmentService
from portfolio.models import Project
from cybersecurity.models import CybersecurityService
from computers.models import ComputerCategory, NetworkService

def home(request):
    education_services = EducationService.objects.all()[:3]
    development_services = DevelopmentService.objects.all()[:3]
    cybersecurity_services = CybersecurityService.objects.filter(is_featured=True)[:3]
    computer_categories = ComputerCategory.objects.filter(is_featured=True)[:2]
    network_services = NetworkService.objects.filter(is_featured=True)[:1]
    testimonials = Testimonial.objects.all()[:3]
    projects = Project.objects.all()[:4]

    context = {
        'education_services': education_services,
        'development_services': development_services,
        'cybersecurity_services': cybersecurity_services,
        'computer_categories': computer_categories,
        'network_services': network_services,
        'testimonials': testimonials,
        'projects': projects,
    }
    return render(request, 'core/home.html', context)

def about(request):
    team_members = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'team_members': team_members,
        'testimonials': testimonials,
    }
    return render(request, 'core/about.html', context)
