from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rdl($@=+0hna&@n1g#!#x+_mk^ma&zio6uphwnivzr63200d2m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Add your domain or allowed IP addresses here for production
ALLOWED_HOSTS = ['*']  # For development; change for production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Add your custom apps
    'accounts',  # The user authentication app
    'service_requests',  # The service request handling app
    'rest_framework',  # For using Django REST Framework
    'storages',  # For managing static files and media with cloud (like AWS, Azure, etc.)
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gas_utility_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add templates directory path
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gas_utility_service.wsgi.application'

# Database Configuration (using MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gas_utility_service',  # Set your MySQL database name here
        'USER': 'myuser',  # Set your MySQL username
        'PASSWORD': 'mypassword',  # Set your MySQL password
        'HOST': 'localhost',  # Or your MySQL host, e.g., 'localhost' or an IP address
        'PORT': '3306',  # Default MySQL port
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Configuring static files storage (for cloud usage)
# If using AWS, Azure, or another cloud service, update accordingly in production
if not DEBUG:
    # For production, use a cloud storage for static files
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
    AWS_ACCESS_KEY_ID = 'your-access-key'
    AWS_SECRET_ACCESS_KEY = 'your-secret-key'
    AWS_S3_REGION_NAME = 'us-west-1'

# Media files (for handling user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Additional settings for managing static files and media in production
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where to collect static files in production

# Security settings for production
SECURE_SSL_REDIRECT = False  # Redirect HTTP to HTTPS in production
CSRF_COOKIE_SECURE = True  # Secure CSRF cookies in production
SESSION_COOKIE_SECURE = True  # Secure session cookies in production
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
