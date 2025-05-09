import os
import django
import datetime
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ricas_it_services.settings')
django.setup()

# Import models after Django setup
from core.models import TeamMember, Testimonial
from education.models import EducationService
from development.models import DevelopmentService
from portfolio.models import Project, ProjectImage
from django.contrib.auth.models import User

def create_superuser():
    """Create a superuser if it doesn't exist"""
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser created successfully!")
    else:
        print("Superuser already exists.")

def populate_team_members():
    """Populate team members"""
    if TeamMember.objects.exists():
        print("Team members already exist. Skipping...")
        return
    
    team_members = [
        {
            'name': 'John Doe',
            'position': 'CEO & Lead Developer',
            'bio': 'John has over 10 years of experience in software development and ICT education. He founded Ricas IT Services with a vision to provide quality technology education and custom software solutions.',
            'image': 'https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
            'order': 1
        },
        {
            'name': 'Jane Smith',
            'position': 'Lead Educator',
            'bio': 'Jane specializes in ICT education for all age groups. With a background in education and computer science, she develops and delivers engaging technology courses that make learning fun and practical.',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=688&q=80',
            'order': 2
        },
        {
            'name': 'Michael Johnson',
            'position': 'Senior Developer',
            'bio': 'Michael is an experienced full-stack developer with expertise in web and mobile application development. He leads our development team and ensures that all projects meet the highest quality standards.',
            'image': 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
            'order': 3
        }
    ]
    
    for member_data in team_members:
        TeamMember.objects.create(**member_data)
    
    print(f"Created {len(team_members)} team members")

def populate_testimonials():
    """Populate testimonials"""
    if Testimonial.objects.exists():
        print("Testimonials already exist. Skipping...")
        return
    
    testimonials = [
        {
            'name': 'Sarah Johnson',
            'position': 'Principal',
            'company': 'Johnson Academy',
            'content': 'The school management system developed by Ricas IT Services has transformed how we operate. Our administrative tasks are now streamlined, and our teachers can focus more on teaching. Highly recommended!',
            'image': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
        },
        {
            'name': 'Michael Brown',
            'position': 'Owner',
            'company': 'Brown\'s Boutique',
            'content': 'Our e-commerce website has seen a 40% increase in sales since Ricas IT Services redesigned it. The mobile-friendly design and improved checkout process have made a significant difference to our business.',
            'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
        },
        {
            'name': 'Emily Davis',
            'position': 'Parent',
            'company': '',
            'content': 'My son has been attending the Scratch Programming course, and I\'m amazed at how much he\'s learned. The instructors make coding fun and engaging, and he\'s already created several games on his own!',
            'image': 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
        }
    ]
    
    for testimonial_data in testimonials:
        Testimonial.objects.create(**testimonial_data)
    
    print(f"Created {len(testimonials)} testimonials")

def populate_education_services():
    """Populate education services"""
    if EducationService.objects.exists():
        print("Education services already exist. Skipping...")
        return
    
    education_services = [
        {
            'title': 'Basic Computer Skills',
            'description': 'This course introduces students to the fundamentals of using computers. Topics include operating systems, file management, internet browsing, email, and basic office applications. Perfect for beginners of all ages who want to build a solid foundation in computer literacy.',
            'age_group': 'all',
            'learning_goals': '- Understand basic computer terminology and components\n- Navigate operating systems confidently\n- Manage files and folders effectively\n- Use internet browsers and email safely\n- Create basic documents using office applications',
            'format': 'in_person',
            'image': 'https://images.unsplash.com/photo-1610986603166-f78428624e76?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80',
            'order': 1
        },
        {
            'title': 'Scratch Programming for Kids',
            'description': 'Introduce your child to the world of programming with Scratch! This visual programming language makes it fun and easy for kids to learn coding concepts while creating their own interactive stories, games, and animations.',
            'age_group': 'kids',
            'learning_goals': '- Understand basic programming concepts\n- Develop computational thinking skills\n- Create interactive stories and games\n- Learn problem-solving techniques\n- Build creativity and confidence in technology',
            'format': 'hybrid',
            'image': 'https://images.unsplash.com/photo-1587620962725-abab7fe55159?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1631&q=80',
            'order': 2
        },
        {
            'title': 'Web Design Fundamentals',
            'description': 'Learn the essentials of web design in this comprehensive course. Students will gain hands-on experience with HTML, CSS, and basic JavaScript, enabling them to create responsive and visually appealing websites from scratch.',
            'age_group': 'teens',
            'learning_goals': '- Understand HTML structure and elements\n- Style web pages using CSS\n- Create responsive layouts for different devices\n- Add interactivity with basic JavaScript\n- Publish and maintain a website',
            'format': 'online',
            'image': 'https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80',
            'order': 3
        },
        {
            'title': 'Digital Marketing Essentials',
            'description': 'This course covers the fundamentals of digital marketing, including social media marketing, email campaigns, SEO, and content creation. Ideal for business owners, entrepreneurs, and professionals looking to enhance their online presence.',
            'age_group': 'adults',
            'learning_goals': '- Develop effective digital marketing strategies\n- Utilize social media platforms for business growth\n- Create engaging content for different channels\n- Understand SEO principles and implementation\n- Analyze marketing performance using analytics tools',
            'format': 'hybrid',
            'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80',
            'order': 4
        }
    ]
    
    for service_data in education_services:
        EducationService.objects.create(**service_data)
    
    print(f"Created {len(education_services)} education services")

def populate_development_services():
    """Populate development services"""
    if DevelopmentService.objects.exists():
        print("Development services already exist. Skipping...")
        return
    
    development_services = [
        {
            'title': 'Custom Web Applications',
            'description': 'We develop tailored web applications that address your specific business needs. Our solutions are scalable, secure, and user-friendly, designed to streamline your operations and enhance productivity.',
            'technologies': 'Django, React, Node.js, PostgreSQL, AWS',
            'image': 'https://images.unsplash.com/photo-1547658719-da2b51169166?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=764&q=80',
            'order': 1
        },
        {
            'title': 'School Management Systems',
            'description': 'Our comprehensive school management systems help educational institutions manage student data, attendance, grades, schedules, and communication with parents. These systems are designed to reduce administrative burden and improve educational outcomes.',
            'technologies': 'Django, PostgreSQL, Bootstrap, jQuery, REST API',
            'image': 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80',
            'order': 2
        },
        {
            'title': 'E-commerce Solutions',
            'description': 'We create custom e-commerce platforms that help businesses sell products and services online. Our solutions include secure payment processing, inventory management, customer accounts, and analytics to drive sales and growth.',
            'technologies': 'Django, React, Stripe, PayPal, PostgreSQL, Redis',
            'image': 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80',
            'order': 3
        },
        {
            'title': 'Mobile App Development',
            'description': 'We develop native and cross-platform mobile applications for iOS and Android. Our mobile solutions are designed to provide excellent user experience, performance, and functionality across different devices and screen sizes.',
            'technologies': 'React Native, Flutter, Firebase, REST API',
            'image': 'https://images.unsplash.com/photo-1551650975-87deedd944c3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1074&q=80',
            'order': 4
        }
    ]
    
    for service_data in development_services:
        DevelopmentService.objects.create(**service_data)
    
    print(f"Created {len(development_services)} development services")

def populate_portfolio():
    """Populate portfolio projects"""
    if Project.objects.exists():
        print("Portfolio projects already exist. Skipping...")
        return
    
    projects = [
        {
            'title': 'Johnson Academy School Management System',
            'description': 'A comprehensive school management system developed for Johnson Academy. The system manages student records, attendance, grades, schedules, and parent communication. It has significantly reduced administrative workload and improved communication between teachers, administrators, and parents.',
            'category': 'web',
            'client': 'Johnson Academy',
            'technologies': 'Django, PostgreSQL, Bootstrap, jQuery, REST API',
            'completion_date': timezone.now() - datetime.timedelta(days=90),
            'image': 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80',
            'order': 1
        },
        {
            'title': 'Brown\'s Boutique E-commerce Platform',
            'description': 'A custom e-commerce platform for Brown\'s Boutique, a fashion retailer. The platform includes product management, secure payment processing, customer accounts, and order tracking. Since launch, the client has seen a 40% increase in online sales.',
            'category': 'web',
            'client': 'Brown\'s Boutique',
            'technologies': 'Django, React, Stripe, PostgreSQL, AWS',
            'completion_date': timezone.now() - datetime.timedelta(days=120),
            'image': 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80',
            'order': 2
        },
        {
            'title': 'HealthTrack Mobile App',
            'description': 'A mobile application for HealthTrack Fitness Center that allows members to book classes, track workouts, monitor progress, and receive personalized fitness recommendations. The app has improved member engagement and retention.',
            'category': 'mobile',
            'client': 'HealthTrack Fitness Center',
            'technologies': 'React Native, Firebase, Node.js',
            'completion_date': timezone.now() - datetime.timedelta(days=60),
            'image': 'https://images.unsplash.com/photo-1551650975-87deedd944c3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1074&q=80',
            'order': 3
        },
        {
            'title': 'City Library Management System',
            'description': 'A comprehensive library management system for the City Public Library. The system manages book inventory, member accounts, borrowing and returns, reservations, and overdue notifications. It has streamlined library operations and improved the user experience for library patrons.',
            'category': 'web',
            'client': 'City Public Library',
            'technologies': 'Django, PostgreSQL, Bootstrap, jQuery',
            'completion_date': timezone.now() - datetime.timedelta(days=180),
            'image': 'https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1290&q=80',
            'order': 4
        }
    ]
    
    for project_data in projects:
        Project.objects.create(**project_data)
    
    print(f"Created {len(projects)} portfolio projects")

if __name__ == '__main__':
    print("Starting database population...")
    create_superuser()
    populate_team_members()
    populate_testimonials()
    populate_education_services()
    populate_development_services()
    populate_portfolio()
    print("Database population completed!")
