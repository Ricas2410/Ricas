from datetime import datetime
from .models import SiteSettings, BannerImage, HomePageSettings

def site_settings(request):
    """
    Context processor to make site settings available to all templates
    """
    try:
        site_settings = SiteSettings.objects.first()
    except:
        site_settings = None
    
    try:
        home_settings = HomePageSettings.objects.first()
    except:
        home_settings = None
    
    # Get all banner images
    try:
        banners = {banner.section: banner for banner in BannerImage.objects.all()}
    except:
        banners = {}
    
    # Format copyright text with current year
    copyright_text = ""
    if site_settings and site_settings.copyright_text:
        current_year = datetime.now().year
        copyright_text = site_settings.copyright_text.replace("{year}", str(current_year))
    
    return {
        'site_settings': site_settings,
        'home_settings': home_settings,
        'banners': banners,
        'copyright_text': copyright_text,
    }
