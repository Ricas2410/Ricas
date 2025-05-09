# Deployment Checklist for Ricas IT Services Website

## Pre-Deployment Tasks

- [ ] Install required packages:
  ```
  pip install -r requirements.txt
  ```

- [ ] Configure environment variables in `.env` file:
  - [ ] Set `SECRET_KEY` to a secure random string
  - [ ] Set `DEBUG=False` for production
  - [ ] Configure database settings if using PostgreSQL
  - [ ] Configure email settings (SMTP)
  - [ ] Set `ECOMMERCE_URL` if applicable

- [ ] Collect static files:
  ```
  python manage.py collectstatic --noinput
  ```

- [ ] Run migrations:
  ```
  python manage.py migrate
  ```

- [ ] Create a superuser:
  ```
  python manage.py createsuperuser
  ```

- [ ] Seed the database with initial data:
  ```
  python seed_data.py
  ```

- [ ] Test the application locally:
  ```
  python manage.py runserver
  ```

## Deployment Options

### Option 1: PythonAnywhere

1. Sign up for a PythonAnywhere account
2. Upload your code to PythonAnywhere
3. Create a virtual environment and install dependencies
4. Configure your web app settings
5. Set up your database
6. Configure environment variables
7. Collect static files
8. Run migrations
9. Create a superuser

### Option 2: Heroku

1. Install the Heroku CLI
2. Login to Heroku:
   ```
   heroku login
   ```
3. Create a new Heroku app:
   ```
   heroku create your-app-name
   ```
4. Add PostgreSQL addon:
   ```
   heroku addons:create heroku-postgresql:mini
   ```
5. Configure environment variables:
   ```
   heroku config:set SECRET_KEY=your_secret_key
   heroku config:set DEBUG=False
   heroku config:set EMAIL_HOST_USER=your_email@gmail.com
   heroku config:set EMAIL_HOST_PASSWORD=your_app_password
   heroku config:set ECOMMERCE_URL=https://shop.ricasitservices.com
   ```
6. Deploy to Heroku:
   ```
   git push heroku main
   ```
7. Run migrations on Heroku:
   ```
   heroku run python manage.py migrate
   ```
8. Create a superuser on Heroku:
   ```
   heroku run python manage.py createsuperuser
   ```
9. Seed the database on Heroku:
   ```
   heroku run python seed_data.py
   ```

### Option 3: VPS (DigitalOcean, AWS, etc.)

1. Set up a server with Ubuntu
2. Install required packages:
   ```
   sudo apt-get update
   sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
   ```
3. Create a PostgreSQL database
4. Clone your repository
5. Set up a virtual environment and install dependencies
6. Configure environment variables
7. Collect static files
8. Run migrations
9. Create a superuser
10. Set up Gunicorn
11. Configure Nginx
12. Set up SSL with Let's Encrypt

## Post-Deployment Tasks

- [ ] Configure the admin site:
  - [ ] Add Site Settings
  - [ ] Add Banner Images
  - [ ] Add Education Services
  - [ ] Add Development Services
  - [ ] Add Cybersecurity Services
  - [ ] Add Computer Categories and Products
  - [ ] Add Network Services
  - [ ] Add Portfolio Items

- [ ] Test all features:
  - [ ] Navigation and dropdowns
  - [ ] Contact form
  - [ ] Service pages
  - [ ] E-commerce redirection
  - [ ] Admin functionality

- [ ] Set up regular backups
- [ ] Configure monitoring
- [ ] Set up error tracking

## Email Configuration

For email functionality, you need to configure SMTP settings:

1. For Gmail:
   - Enable 2-factor authentication
   - Generate an App Password
   - Use the App Password in your `.env` file

2. For other providers:
   - Update the `EMAIL_HOST` and `EMAIL_PORT` settings
   - Provide the correct username and password

3. Test email functionality:
   - Try submitting the contact form
   - Check admin notifications

## Security Considerations

- [ ] Ensure `DEBUG=False` in production
- [ ] Use a strong, unique `SECRET_KEY`
- [ ] Configure SSL/HTTPS
- [ ] Set up proper file permissions
- [ ] Regularly update dependencies
- [ ] Implement rate limiting for forms
- [ ] Set up firewall rules
- [ ] Configure database backups
