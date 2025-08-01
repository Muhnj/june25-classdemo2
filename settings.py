import os
from pathlib import Path

# Base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep the secret key secret in production!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure-test-key")

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]  # For CI/CD and local dev

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Your Django apps
    "greeting",  # ← Make sure this matches your app name

    # Third-party apps
    "pytest_django",  # Optional but safe to include
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "june25-classdemo2.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "june25-classdemo2.wsgi.application"

# Database (SQLite is easiest for CI)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"

# Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
