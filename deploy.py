#!/usr/bin/env python
"""
Deployment script for Ricas IT Services website.
This script collects static files and prepares the site for deployment.
"""

import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and print the output."""
    print(f"Running: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in process.stdout:
        print(line.decode('utf-8').strip())
    process.wait()
    return process.returncode

def main():
    """Main function to prepare the site for deployment."""
    print("Preparing Ricas IT Services website for deployment...")
    
    # Collect static files
    print("\n1. Collecting static files...")
    if run_command("python manage.py collectstatic --noinput") != 0:
        print("Error collecting static files.")
        return 1
    
    # Run migrations
    print("\n2. Running migrations...")
    if run_command("python manage.py migrate") != 0:
        print("Error running migrations.")
        return 1
    
    # Check for deployment environment
    if os.environ.get('HEROKU'):
        print("\nDeploying to Heroku...")
    elif os.environ.get('PYTHONANYWHERE'):
        print("\nDeploying to PythonAnywhere...")
    else:
        print("\nDeployment environment not detected.")
        print("Set HEROKU=1 or PYTHONANYWHERE=1 environment variable to indicate deployment target.")
    
    print("\nDeployment preparation complete!")
    print("Next steps:")
    print("1. Commit your changes to git")
    print("2. Push to your deployment platform")
    print("3. Set up your environment variables (SECRET_KEY, DEBUG, DATABASE_URL)")
    print("4. Create a superuser and configure the admin settings")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
