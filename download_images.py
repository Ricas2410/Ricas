import os
import django
import requests
from django.core.files.base import ContentFile
from django.conf import settings
import urllib.parse
import time

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ricas_it_services.settings')
django.setup()

# Import models after Django setup
from settings.models import SiteSettings, BannerImage

def download_image(url, filename, save_path):
    """
    Download image from URL and save it to the specified path
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Download image
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded {filename} successfully")
            return True
        else:
            print(f"Failed to download {filename}: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")
        return False

def download_site_logo():
    """Download and save site logo"""
    site_settings = SiteSettings.objects.first()
    if not site_settings:
        print("Site settings not found")
        return

    # Logo URL
    logo_url = "https://via.placeholder.com/200x200?text=Ricas+IT"
    logo_filename = "ricas_logo.png"
    logo_path = os.path.join(settings.MEDIA_ROOT, 'site', logo_filename)

    if download_image(logo_url, logo_filename, logo_path):
        # Update site settings with the new logo
        relative_path = os.path.join('site', logo_filename)
        site_settings.site_logo = relative_path
        site_settings.save()
        print("Site logo updated successfully")

def download_favicon():
    """Download and save favicon"""
    site_settings = SiteSettings.objects.first()
    if not site_settings:
        print("Site settings not found")
        return

    # Favicon URL
    favicon_url = "https://via.placeholder.com/32x32?text=R"
    favicon_filename = "favicon.png"
    favicon_path = os.path.join(settings.MEDIA_ROOT, 'site', favicon_filename)

    if download_image(favicon_url, favicon_filename, favicon_path):
        # Update site settings with the new favicon
        relative_path = os.path.join('site', favicon_filename)
        site_settings.favicon = relative_path
        site_settings.save()
        print("Favicon updated successfully")

def download_banner_images():
    """Download and save banner images"""
    banner_data = [
        {
            'section': 'home_hero',
            'url': 'https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'
        },
        {
            'section': 'about_hero',
            'url': 'https://images.unsplash.com/photo-1552581234-26160f608093?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'
        },
        {
            'section': 'education_hero',
            'url': 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1122&q=80'
        },
        {
            'section': 'development_hero',
            'url': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1172&q=80'
        },
        {
            'section': 'portfolio_hero',
            'url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1115&q=80'
        },
        {
            'section': 'contact_hero',
            'url': 'https://images.unsplash.com/photo-1423666639041-f56000c27a9a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1174&q=80'
        },
        {
            'section': 'cta_image',
            'url': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'
        }
    ]

    for data in banner_data:
        try:
            banner = BannerImage.objects.get(section=data['section'])

            # Generate filename from URL
            url_parts = urllib.parse.urlparse(data['url'])
            filename = os.path.basename(url_parts.path)
            if not filename or '.' not in filename:
                filename = f"{data['section']}.jpg"

            # Download image
            image_path = os.path.join(settings.MEDIA_ROOT, 'banners', filename)
            if download_image(data['url'], filename, image_path):
                # Update banner with the new image
                relative_path = os.path.join('banners', filename)
                banner.image = relative_path
                banner.save()
                print(f"Banner image for {data['section']} updated successfully")

                # Add a small delay to avoid rate limiting
                time.sleep(1)
        except BannerImage.DoesNotExist:
            print(f"Banner for section {data['section']} not found")
        except Exception as e:
            print(f"Error updating banner for {data['section']}: {str(e)}")

if __name__ == '__main__':
    print("Starting image downloads...")

    # Create media directories if they don't exist
    os.makedirs(os.path.join(settings.MEDIA_ROOT, 'site'), exist_ok=True)
    os.makedirs(os.path.join(settings.MEDIA_ROOT, 'banners'), exist_ok=True)

    download_site_logo()
    download_favicon()
    download_banner_images()

    print("Image downloads completed!")
