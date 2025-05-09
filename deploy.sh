#!/bin/bash
# Deployment script for Ricas IT Services website

echo "Preparing Ricas IT Services website for deployment..."

# Collect static files
echo -e "\n1. Collecting static files..."
python manage.py collectstatic --noinput
if [ $? -ne 0 ]; then
    echo "Error collecting static files."
    exit 1
fi

# Run migrations
echo -e "\n2. Running migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error running migrations."
    exit 1
fi

# Check for deployment environment
if [ ! -z "$HEROKU" ]; then
    echo -e "\nDeploying to Heroku..."
elif [ ! -z "$PYTHONANYWHERE" ]; then
    echo -e "\nDeploying to PythonAnywhere..."
else
    echo -e "\nDeployment environment not detected."
    echo "Set HEROKU=1 or PYTHONANYWHERE=1 environment variable to indicate deployment target."
fi

echo -e "\nDeployment preparation complete!"
echo "Next steps:"
echo "1. Commit your changes to git"
echo "2. Push to your deployment platform"
echo "3. Set up your environment variables (SECRET_KEY, DEBUG, DATABASE_URL)"
echo "4. Create a superuser and configure the admin settings"

exit 0
