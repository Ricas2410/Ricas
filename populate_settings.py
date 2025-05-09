import os
import django
import datetime
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ricas_it_services.settings')
django.setup()

# Import models after Django setup
from settings.models import SiteSettings, BannerImage, HomePageSettings

def populate_site_settings():
    """Populate site settings if they don't exist"""
    if SiteSettings.objects.exists():
        print("Site settings already exist. Skipping...")
        return

    # Create site settings
    site_settings = SiteSettings(
        site_name="Ricas IT Services",
        email="services.ricas@gmail.com",
        phone="0505584553",
        address="Accra, Ghana",
        business_hours="Mon-Fri: 9:00 AM - 5:00 PM",
        footer_text="Providing quality ICT education and professional software development services to help individuals and businesses thrive in the digital world.",
        copyright_text="© {year} Ricas IT Services. All rights reserved.",
        meta_description="Ricas IT Services provides quality ICT education for all ages and professional software development services for businesses in Ghana.",
        meta_keywords="ICT education, software development, web development, mobile apps, Ghana, Accra"
    )

    site_settings.save()
    print("Site settings created successfully!")

def populate_banner_images():
    """Populate banner images if they don't exist"""
    if BannerImage.objects.exists():
        print("Banner images already exist. Skipping...")
        return

    banner_data = [
        {
            'section': 'home_hero',
            'title': 'Empowering Through Technology',
            'subtitle': 'Quality ICT education and software development services',
        },
        {
            'section': 'about_hero',
            'title': 'About Ricas IT Services',
            'subtitle': 'Learn more about our mission and values',
        },
        {
            'section': 'education_hero',
            'title': 'ICT Education Services',
            'subtitle': 'Practical technology education for all ages',
        },
        {
            'section': 'development_hero',
            'title': 'Software Development Services',
            'subtitle': 'Custom solutions for your business needs',
        },
        {
            'section': 'portfolio_hero',
            'title': 'Our Portfolio',
            'subtitle': 'Explore our past projects and success stories',
        },
        {
            'section': 'contact_hero',
            'title': 'Contact Us',
            'subtitle': 'Get in touch with our team',
        },
        {
            'section': 'cta_image',
            'title': 'Call to Action',
            'subtitle': 'Students in IT lab',
        }
    ]

    for data in banner_data:
        banner = BannerImage(
            section=data['section'],
            title=data['title'],
            subtitle=data['subtitle']
        )

        banner.save()

    print(f"Created {len(banner_data)} banner images")
    print("NOTE: You'll need to upload banner images through the admin interface.")

def populate_home_page_settings():
    """Populate home page settings if they don't exist"""
    if HomePageSettings.objects.exists():
        print("Home page settings already exist. Skipping...")
        return

    home_settings = HomePageSettings(
        hero_title="Empowering Through Technology",
        hero_subtitle="We provide quality ICT education for all ages and professional software development services tailored to your business needs.",

        services_title="Our Services",
        services_subtitle="Discover how we can help you or your organization thrive in the digital world",

        education_title="ICT Education Services",
        education_subtitle="Practical technology education for all ages",

        development_title="Software Development Services",
        development_subtitle="Custom solutions tailored to your business needs",

        portfolio_title="Our Portfolio",
        portfolio_subtitle="Check out some of our recent projects",

        testimonial_title="What Our Clients Say",
        testimonial_subtitle="Testimonials from our satisfied clients",

        cta_title="Ready to Transform Your Digital Experience?",
        cta_subtitle="Contact us today to discuss your ICT education or software development needs. Our team is ready to help you achieve your goals."
    )

    home_settings.save()
    print("Home page settings created successfully!")

if __name__ == '__main__':
    print("Starting site settings population...")
    populate_site_settings()
    populate_banner_images()
    populate_home_page_settings()
    print("Site settings population completed!")
