from django.shortcuts import render, get_object_or_404
from .models import Project

def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)
