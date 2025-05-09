@echo off
REM Deployment script for Ricas IT Services website

echo Preparing Ricas IT Services website for deployment...

REM Collect static files
echo.
echo 1. Collecting static files...
python manage.py collectstatic --noinput
if %ERRORLEVEL% NEQ 0 (
    echo Error collecting static files.
    exit /b 1
)

REM Run migrations
echo.
echo 2. Running migrations...
python manage.py migrate
if %ERRORLEVEL% NEQ 0 (
    echo Error running migrations.
    exit /b 1
)

REM Check for deployment environment
if defined HEROKU (
    echo.
    echo Deploying to Heroku...
) else if defined PYTHONANYWHERE (
    echo.
    echo Deploying to PythonAnywhere...
) else (
    echo.
    echo Deployment environment not detected.
    echo Set HEROKU=1 or PYTHONANYWHERE=1 environment variable to indicate deployment target.
)

echo.
echo Deployment preparation complete!
echo Next steps:
echo 1. Commit your changes to git
echo 2. Push to your deployment platform
echo 3. Set up your environment variables (SECRET_KEY, DEBUG, DATABASE_URL)
echo 4. Create a superuser and configure the admin settings

exit /b 0
