# Todo application

This is a sample Todo list application that uses

- JavaScript and React for the front-end component
- Python and the Django for the server side component
- MySQL for the database

References:

https://tutorial.djangogirls.org/en/

# Mac laptop setup

This assumes you have git installed and a GitHub or similar account

Install Homebrew (https://brew.sh/)

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Install python3

One option is to download it from https://www.python.org/downloads/mac-osx/

Another option is to use Homebrew:

`brew install python`

Install MySQL

`brew install mysql`

Once the installation finishes, several useful messages are displayed:

We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

To have launchd start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  mysql.server start

# Configure MySQL

`mysql.server start`
`mysql_secure_installation`

# When finished, stop MySQL

`mysql.server stop`

# Load the timezone information

`mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root mysql -p`

# Create the database

`mysql -u root -h localhost -p`
`mysql> create database django character set utf8;`

# Create a working directory

`mkdir django`
`cd django`

# Define a python virtual environment and activate it

`python3 -m venv pyvenv`
`source ./pyvenv/bin/activate`

Note:  When finished using the virtual environment it can be deactivated with

`deactivate`

# Update pip

`python -m pip install --upgrade pip`

# Create the file requirements.txt with the following entry

Django

# Install Django

`pip install -r requirements.txt`

# Install mysqlclient

`pip install mysqlclient`

# If desired, create a PythonAnywhere account to host the application

https://www.pythonanywhere.com/

# Create a Django project

`django-admin startproject mysite .`

# Change the language code in mysite/settings.py

TIME_ZONE = 'America/Chicago'

# At the top of mysite/settings.py add

import os

It should look like this:

from pathlib import Path
import os

Add the STATIC_ROOT definition under STATIC_URL

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

Change ALLOWED_HOSTS

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

Modify the database settings in mysite/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '~/Documents/.mycreds/my.cnf',
        },
    }
}

# Create the MySQL default file (my.cnf) listed above

[client]
database = django
user = root
password = XXXX
default-character-set = utf8

# Set up the database

`python manage.py migrate`

# Start the server

`python manage.py runserver`

# Access the server in a browser

`http://127.0.0.1:8000/`

# Create the todo application

`python manage.py startapp todo`

## Add application to Django - Edit mysite/settings.py to look as follows:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo.apps.TodoConfig',
]

## Create the todo app model in todo/models.py

from django.conf import settings
from django.db import models
from django.utils import timezone


class Item(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    task_complete = models.BooleanField(default=False)
    completion_date = models.DateTimeField(blank=True, null=True)
    task_archived = models.BooleanField(default=False)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

## Create the tables for the model in the database

python manage.py makemigrations todo
python manage.py migrate todo

## Make the model visible on the Django admin page

Edit todo/admin.py to read

from django.contrib import admin
from .models import Item

admin.site.register(Item)

## Add a site admin user (e.g. - a user named siteadmin)

python manage.py createsuperuser

## Start the server and navigate to http://localhost:8000/admin

python manage.py runserver
