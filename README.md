# Ricas IT Services Website

A comprehensive website for Ricas IT Services, featuring ICT education, software development, cybersecurity, and computer sales services.

## Features

- ICT Education Services
- Software Development Services
- Cybersecurity Services
- Computer Sales & Network Services
- Portfolio Showcase
- Contact Form
- Admin-manageable content

## Tech Stack

- Django 5.2
- Bootstrap 5
- SQLite (development) / PostgreSQL (production)
- Whitenoise for static files
- Responsive design

## Local Development

1. Clone the repository
```bash
git clone https://github.com/yourusername/ricas-it-services.git
cd ricas-it-services
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

7. Access the site at http://127.0.0.1:8000/

## Email Configuration

The website uses SMTP for sending emails from the contact form. To configure email:

1. For Gmail:
   - Enable 2-factor authentication on your Google account
   - Generate an App Password (Google Account > Security > App Passwords)
   - Add the following to your `.env` file:
     ```
     EMAIL_HOST=smtp.gmail.com
     EMAIL_PORT=587
     EMAIL_USE_TLS=True
     EMAIL_HOST_USER=your-email@gmail.com
     EMAIL_HOST_PASSWORD=your-app-password
     DEFAULT_FROM_EMAIL=your-email@gmail.com
     ```

2. Test email functionality:
   ```
   python test_email.py
   ```

3. Email Features:
   - Contact form submissions send notifications to the admin
   - Confirmation emails are sent to users who submit the contact form
   - Professional email templates with branding

## Deployment

### Heroku Deployment

1. Create a Heroku account and install the Heroku CLI
2. Login to Heroku
```bash
heroku login
```

3. Create a new Heroku app
```bash
heroku create your-app-name
```

4. Add PostgreSQL addon
```bash
heroku addons:create heroku-postgresql:mini
```

5. Configure environment variables
```bash
heroku config:set SECRET_KEY=your_secret_key
heroku config:set DEBUG=False
heroku config:set EMAIL_HOST_USER=your_email@gmail.com
heroku config:set EMAIL_HOST_PASSWORD=your_app_password
heroku config:set DEFAULT_FROM_EMAIL=your_email@gmail.com
heroku config:set SITE_NAME="Ricas IT Services"
heroku config:set SITE_URL=https://your-app-name.herokuapp.com
heroku config:set ADMIN_EMAIL=services.ricas@gmail.com
```

6. Deploy to Heroku
```bash
git push heroku main
```

7. Run migrations on Heroku
```bash
heroku run python manage.py migrate
```

8. Create a superuser on Heroku
```bash
heroku run python manage.py createsuperuser
```

### PythonAnywhere Deployment

1. Sign up for a PythonAnywhere account
2. Upload your code to PythonAnywhere
3. Create a virtual environment and install dependencies
4. Configure your web app settings
5. Set up your database
6. Configure environment variables
7. Collect static files
8. Run migrations
9. Create a superuser

## Admin Setup

After deployment, log in to the admin panel at `/admin` and:

1. Create Site Settings
2. Add Banner Images for different sections
3. Add Education Services
4. Add Development Services
5. Add Cybersecurity Services
6. Add Computer Categories and Products
7. Add Network Services
8. Add Portfolio Items
9. Configure the E-commerce URL for computer sales

## License

This project is licensed under the MIT License - see the LICENSE file for details.
