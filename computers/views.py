from django.shortcuts import render, get_object_or_404, redirect
from .models import ComputerCategory, ComputerProduct, NetworkService
from settings.models import BannerImage, SiteSettings

def computer_categories(request):
    """View for listing all computer categories"""
    categories = ComputerCategory.objects.all()

    # Get banner images
    banners = {}
    for banner in BannerImage.objects.all():
        banners[banner.section] = banner

    # Get site settings
    site_settings = SiteSettings.objects.first()

    context = {
        'categories': categories,
        'banners': banners,
        'site_settings': site_settings,
    }

    return render(request, 'computers/categories.html', context)

def computer_category_detail(request, slug):
    """View for a single computer category"""
    category = get_object_or_404(ComputerCategory, slug=slug)
    products = category.products.all()

    # Get banner images
    banners = {}
    for banner in BannerImage.objects.all():
        banners[banner.section] = banner

    # Get site settings
    site_settings = SiteSettings.objects.first()

    context = {
        'category': category,
        'products': products,
        'banners': banners,
        'site_settings': site_settings,
    }

    return render(request, 'computers/category_detail.html', context)

def computer_product_detail(request, category_slug, product_slug):
    """View for a single computer product"""
    product = get_object_or_404(ComputerProduct, slug=product_slug, category__slug=category_slug)
    related_products = ComputerProduct.objects.filter(category=product.category).exclude(id=product.id)[:3]

    # Get banner images
    banners = {}
    for banner in BannerImage.objects.all():
        banners[banner.section] = banner

    # Get site settings
    site_settings = SiteSettings.objects.first()

    context = {
        'product': product,
        'related_products': related_products,
        'banners': banners,
        'site_settings': site_settings,
    }

    return render(request, 'computers/product_detail.html', context)

def network_services(request):
    """View for listing all network services"""
    services = NetworkService.objects.all()

    # Get banner images
    banners = {}
    for banner in BannerImage.objects.all():
        banners[banner.section] = banner

    context = {
        'services': services,
        'banners': banners,
    }

    return render(request, 'computers/network_services.html', context)

def network_service_detail(request, slug):
    """View for a single network service"""
    service = get_object_or_404(NetworkService, slug=slug)
    related_services = NetworkService.objects.exclude(id=service.id)[:3]

    # Get banner images
    banners = {}
    for banner in BannerImage.objects.all():
        banners[banner.section] = banner

    context = {
        'service': service,
        'related_services': related_services,
        'banners': banners,
    }

    return render(request, 'computers/network_service_detail.html', context)

def redirect_to_ecommerce(request):
    """Redirect to the e-commerce website"""
    site_settings = SiteSettings.objects.first()

    if site_settings and site_settings.ecommerce_url:
        return redirect(site_settings.ecommerce_url)
    else:
        # If no e-commerce URL is set, redirect to the computer categories page
        return redirect('computer_categories')
