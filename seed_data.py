#!/usr/bin/env python
"""
Script to seed the database with sample data for Ricas IT Services website.
"""

import os
import django
import sys

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ricas_it_services.settings')
django.setup()

from django.contrib.auth.models import User
from settings.models import SiteSettings, BannerImage, HomePageSettings
from cybersecurity.models import CybersecurityService, CybersecurityFeature, CybersecurityTestimonial
from computers.models import ComputerCategory, ComputerProduct, NetworkService

def create_superuser():
    """Create a superuser if one doesn't exist."""
    if not User.objects.filter(is_superuser=True).exists():
        print("Creating superuser...")
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print("Superuser created successfully.")
    else:
        print("Superuser already exists.")

def create_site_settings():
    """Create site settings if they don't exist."""
    if not SiteSettings.objects.exists():
        print("Creating site settings...")
        SiteSettings.objects.create(
            site_name="Ricas IT Services",
            email="services.ricas@gmail.com",
            phone="0505584553",
            address="Accra, Ghana",
            business_hours="Mon-Fri: 9:00 AM - 5:00 PM",
            footer_text="Providing quality ICT education, software development, cybersecurity, and computer sales services to help individuals and businesses thrive in the digital world.",
            ecommerce_url="https://shop.ricasitservices.com",
            meta_description="Ricas IT Services provides ICT education, software development, cybersecurity, and computer sales services in Ghana.",
            meta_keywords="ICT education, software development, cybersecurity, computer sales, Ghana"
        )
        print("Site settings created successfully.")
    else:
        print("Site settings already exist.")

def create_home_page_settings():
    """Create home page settings if they don't exist."""
    if not HomePageSettings.objects.exists():
        print("Creating home page settings...")
        HomePageSettings.objects.create(
            hero_title="Empowering Through Technology",
            hero_subtitle="We provide quality ICT education, software development, cybersecurity, and computer sales services tailored to your needs.",
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
            cta_subtitle="Contact us today to discuss your ICT education, software development, cybersecurity, or computer needs. Our team is ready to help you achieve your goals."
        )
        print("Home page settings created successfully.")
    else:
        print("Home page settings already exist.")

def create_cybersecurity_services():
    """Create sample cybersecurity services."""
    if CybersecurityService.objects.count() == 0:
        print("Creating cybersecurity services...")
        
        # Security Audit Service
        security_audit = CybersecurityService.objects.create(
            title="Security Audits",
            slug="security-audits",
            description="Our comprehensive security audit identifies vulnerabilities in your systems and provides actionable recommendations to improve your security posture. We assess your hardware, software, networks, and security policies to ensure you're protected against common threats.",
            icon="fa-search",
            is_featured=True,
            order=1
        )
        
        CybersecurityFeature.objects.create(
            service=security_audit,
            title="Vulnerability Assessment",
            description="Identify security weaknesses in your systems",
            icon="fa-bug"
        )
        
        CybersecurityFeature.objects.create(
            service=security_audit,
            title="Policy Review",
            description="Evaluate your security policies and procedures",
            icon="fa-file-alt"
        )
        
        # Secure Wi-Fi Service
        secure_wifi = CybersecurityService.objects.create(
            title="Secure Wi-Fi Setup",
            slug="secure-wifi-setup",
            description="We set up and configure your Wi-Fi network with proper security measures to prevent unauthorized access and protect your data. Our service includes secure router configuration, encryption setup, guest network isolation, and regular security updates.",
            icon="fa-wifi",
            is_featured=True,
            order=2
        )
        
        CybersecurityFeature.objects.create(
            service=secure_wifi,
            title="Encrypted Connections",
            description="WPA3 encryption for maximum security",
            icon="fa-lock"
        )
        
        CybersecurityFeature.objects.create(
            service=secure_wifi,
            title="Guest Network",
            description="Isolated guest network to protect your main network",
            icon="fa-user-friends"
        )
        
        # Antivirus Protection
        antivirus = CybersecurityService.objects.create(
            title="Antivirus & System Protection",
            slug="antivirus-protection",
            description="We install and configure robust antivirus and anti-malware solutions to protect your devices from threats. Our service includes software installation, configuration, scheduled scans, real-time protection, and regular updates to ensure ongoing security.",
            icon="fa-shield-alt",
            is_featured=True,
            order=3
        )
        
        CybersecurityFeature.objects.create(
            service=antivirus,
            title="Real-time Protection",
            description="Continuous monitoring for threats",
            icon="fa-clock"
        )
        
        CybersecurityFeature.objects.create(
            service=antivirus,
            title="Automatic Updates",
            description="Always up-to-date protection against new threats",
            icon="fa-sync"
        )
        
        # Online Safety Training
        safety_training = CybersecurityService.objects.create(
            title="Online Safety Training",
            slug="online-safety-training",
            description="We provide practical training sessions to help individuals and organizations stay safe online. Our training covers recognizing phishing attempts, creating strong passwords, safe browsing habits, social media privacy, and protecting personal information.",
            icon="fa-user-shield",
            is_featured=False,
            order=4
        )
        
        # Email Security
        email_security = CybersecurityService.objects.create(
            title="Email & Account Security",
            slug="email-security",
            description="We secure your email accounts and online services against unauthorized access and phishing attacks. Our service includes setting up two-factor authentication, secure password management, email filtering, and phishing protection.",
            icon="fa-envelope-open-text",
            is_featured=False,
            order=5
        )
        
        # Website Protection
        website_protection = CybersecurityService.objects.create(
            title="Website Protection",
            slug="website-protection",
            description="We secure your website against common attacks and vulnerabilities. Our service includes SSL certificate installation, security plugin configuration, regular updates, malware scanning, and backup solutions to keep your website safe and operational.",
            icon="fa-globe-americas",
            is_featured=False,
            order=6
        )
        
        # Data Backup
        data_backup = CybersecurityService.objects.create(
            title="Data Backup & Recovery",
            slug="data-backup-recovery",
            description="We implement reliable backup solutions to protect your important data from loss due to hardware failure, ransomware, or accidental deletion. Our service includes automated backup setup, secure storage configuration, and recovery testing.",
            icon="fa-database",
            is_featured=False,
            order=7
        )
        
        print("Cybersecurity services created successfully.")
    else:
        print("Cybersecurity services already exist.")

def create_computer_categories():
    """Create sample computer categories and products."""
    if ComputerCategory.objects.count() == 0:
        print("Creating computer categories and products...")
        
        # Laptops Category
        laptops = ComputerCategory.objects.create(
            name="Laptops",
            slug="laptops",
            description="High-quality laptops for students, professionals, and businesses. We offer a range of options from budget-friendly models to high-performance workstations.",
            is_featured=True,
            order=1
        )
        
        ComputerProduct.objects.create(
            category=laptops,
            name="Student Laptop Package",
            slug="student-laptop-package",
            description="Affordable laptop package for students, including a reliable laptop, basic software, and protective case. Perfect for schoolwork, research, and basic computing needs.",
            is_featured=True,
            order=1
        )
        
        ComputerProduct.objects.create(
            category=laptops,
            name="Business Laptop Package",
            slug="business-laptop-package",
            description="Professional laptop package for business users, including a high-performance laptop, productivity software, and security features. Ideal for office work, presentations, and multitasking.",
            is_featured=True,
            order=2
        )
        
        # Desktops Category
        desktops = ComputerCategory.objects.create(
            name="Desktops",
            slug="desktops",
            description="Powerful desktop computers for home, office, and lab use. We offer customizable options to meet your specific computing needs.",
            is_featured=True,
            order=2
        )
        
        ComputerProduct.objects.create(
            category=desktops,
            name="Office Desktop Package",
            slug="office-desktop-package",
            description="Complete desktop package for office use, including a reliable desktop computer, monitor, keyboard, mouse, and productivity software. Perfect for everyday business tasks.",
            is_featured=True,
            order=1
        )
        
        ComputerProduct.objects.create(
            category=desktops,
            name="Computer Lab Package",
            slug="computer-lab-package",
            description="Comprehensive desktop package for school computer labs, including multiple desktop computers, monitors, keyboards, mice, and educational software. Ideal for creating a learning environment.",
            is_featured=True,
            order=2
        )
        
        # Accessories Category
        accessories = ComputerCategory.objects.create(
            name="Accessories",
            slug="accessories",
            description="Essential computer accessories to enhance your computing experience. We offer a wide range of peripherals, storage devices, and more.",
            is_featured=True,
            order=3
        )
        
        ComputerProduct.objects.create(
            category=accessories,
            name="External Hard Drives",
            slug="external-hard-drives",
            description="Reliable external hard drives for data backup and storage. Available in various capacities to meet your storage needs.",
            is_featured=False,
            order=1
        )
        
        ComputerProduct.objects.create(
            category=accessories,
            name="Printers & Scanners",
            slug="printers-scanners",
            description="High-quality printers and scanners for home and office use. We offer inkjet, laser, and multifunction options.",
            is_featured=False,
            order=2
        )
        
        # Lab Equipment Category
        lab_equipment = ComputerCategory.objects.create(
            name="Lab Equipment",
            slug="lab-equipment",
            description="Specialized equipment for computer labs in schools and training centers. We offer complete lab setup solutions.",
            is_featured=False,
            order=4
        )
        
        ComputerProduct.objects.create(
            category=lab_equipment,
            name="Computer Lab Furniture",
            slug="computer-lab-furniture",
            description="Ergonomic furniture designed specifically for computer labs, including desks, chairs, and storage solutions.",
            is_featured=False,
            order=1
        )
        
        ComputerProduct.objects.create(
            category=lab_equipment,
            name="Networking Equipment",
            slug="networking-equipment",
            description="Essential networking equipment for computer labs, including switches, routers, and cabling solutions.",
            is_featured=False,
            order=2
        )
        
        print("Computer categories and products created successfully.")
    else:
        print("Computer categories already exist.")

def create_network_services():
    """Create sample network services."""
    if NetworkService.objects.count() == 0:
        print("Creating network services...")
        
        NetworkService.objects.create(
            title="Home Network Setup",
            slug="home-network-setup",
            description="We design and install reliable, secure home networks that connect all your devices seamlessly. Our service includes router configuration, Wi-Fi optimization, device connection, and security setup to ensure your home network is fast, reliable, and protected.",
            icon="fa-home",
            is_featured=True,
            order=1
        )
        
        NetworkService.objects.create(
            title="School Network Installation",
            slug="school-network-installation",
            description="We design and implement comprehensive network solutions for educational institutions. Our service includes network planning, equipment installation, Wi-Fi coverage, computer lab setup, and ongoing support to create a reliable infrastructure for learning.",
            icon="fa-school",
            is_featured=True,
            order=2
        )
        
        NetworkService.objects.create(
            title="Business Network Solutions",
            slug="business-network-solutions",
            description="We provide professional network solutions for businesses of all sizes. Our service includes network design, equipment selection, installation, configuration, security implementation, and maintenance to support your business operations.",
            icon="fa-building",
            is_featured=True,
            order=3
        )
        
        NetworkService.objects.create(
            title="Network Troubleshooting",
            slug="network-troubleshooting",
            description="We diagnose and resolve network issues to minimize downtime and ensure optimal performance. Our service includes identifying connectivity problems, resolving speed issues, fixing device conflicts, and optimizing network performance.",
            icon="fa-tools",
            is_featured=False,
            order=4
        )
        
        NetworkService.objects.create(
            title="Network Security Implementation",
            slug="network-security-implementation",
            description="We implement comprehensive security measures to protect your network from unauthorized access and cyber threats. Our service includes firewall setup, secure Wi-Fi configuration, access control, intrusion detection, and security monitoring.",
            icon="fa-lock",
            is_featured=False,
            order=5
        )
        
        print("Network services created successfully.")
    else:
        print("Network services already exist.")

def create_cybersecurity_testimonials():
    """Create sample cybersecurity testimonials."""
    if CybersecurityTestimonial.objects.count() == 0:
        print("Creating cybersecurity testimonials...")
        
        CybersecurityTestimonial.objects.create(
            name="Sarah Johnson",
            position="Principal",
            company="Accra International School",
            content="Ricas IT Services helped us secure our school's network and protect our students' data. Their cybersecurity audit identified several vulnerabilities we weren't aware of, and their team implemented practical solutions that were easy for our staff to maintain. We now feel confident that our digital resources are well-protected.",
            is_featured=True
        )
        
        CybersecurityTestimonial.objects.create(
            name="Michael Osei",
            position="Owner",
            company="Osei's Pharmacy",
            content="As a small business handling sensitive customer information, cybersecurity was a major concern for us. Ricas IT Services provided affordable security solutions that were tailored to our needs. Their team set up secure systems for our patient data and trained our staff on best practices. Highly recommended!",
            is_featured=True
        )
        
        CybersecurityTestimonial.objects.create(
            name="Grace Mensah",
            position="IT Manager",
            company="Ghana First Bank",
            content="We engaged Ricas IT Services for a comprehensive security audit of our systems. Their thorough approach and detailed recommendations helped us strengthen our security posture significantly. They understand both technical aspects and practical implementation, making them an excellent partner for cybersecurity services.",
            is_featured=True
        )
        
        print("Cybersecurity testimonials created successfully.")
    else:
        print("Cybersecurity testimonials already exist.")

def main():
    """Main function to seed the database."""
    print("Seeding database with sample data...")
    
    create_superuser()
    create_site_settings()
    create_home_page_settings()
    create_cybersecurity_services()
    create_computer_categories()
    create_network_services()
    create_cybersecurity_testimonials()
    
    print("\nDatabase seeding complete!")
    print("You can now log in to the admin panel at /admin with:")
    print("Username: admin")
    print("Password: admin123")
    print("\nIMPORTANT: Change the admin password immediately in a production environment.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
