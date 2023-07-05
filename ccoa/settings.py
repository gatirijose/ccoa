from pathlib import Path
import os
import cloudinary

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'bootstrap5',
    'cloudinary',
    'cloudinary_storage',
    "bootstrap_datepicker_plus",
    'tinymce',
    'rest_framework',
    "corsheaders",
    'accounts.apps.AccountsConfig',
    'posts.apps.PostsConfig',
    'sendemail',
]

<<<<<<< HEAD

=======
CSRF_TRUSTED_ORIGINS = [
        "http://0.0.0.0",
        "http://localhost",
        'https://8000-gatirijose-ccoaupdated-qslpdu11mur.ws-eu101.gitpod.io/'
        "https://8000-gatirijose-ccoaupdated-rs7bbktqai7.ws-eu100.gitpod.io",
        "https://www.youtube.com",
]
>>>>>>> 7fee1cbfaca008b984cedf02cc51169bee721266


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

ROOT_URLCONF = "ccoa.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "ccoa.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

######################################
########            ##################
######################################

AUTH_USER_MODEL = 'accounts.customuser'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / ''
MEDIA_URL = ''

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

cloudinary.config(
    cloud_name=os.environ['CLOUD_NAME'],
    api_key=os.environ['API_KEY'],
    api_secret=os.environ['API_SECRET'],
)

DEFAULT_FROM_EMAIL = "christcovenant2010@gmail.com"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BOOTSTRAP_DATEPICKER_PLUS = {
    "options": {
        "locale": "en",
    },
    "variant_options": {

        "date": {
            "format": "YYYY-MM-DD",
        },
    }
}


REST_FRAMEWORK = { 
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        ],
}

CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://localhost:8000",
)

CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"] 