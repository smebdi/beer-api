"""
Django settings for beer project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# for Heroku setup
DJANGO_PROJECT_DIR = os.path.dirname(BASE_DIR)
PROJECT_DIR = os.path.dirname(DJANGO_PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o#sy0)(9$=+l_o&*0n!y^snz53gx8=*f#j1jc!u92^4&lhjj&8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'beerapp',
    'beer',
]

MIDDLEWARE = [
    'django.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'beer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), 
            os.path.join(BASE_DIR, 'templates/registration')
        ],
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

WSGI_APPLICATION = 'beer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
) 

# for Heroku setup
STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')

# authentication
LOGIN_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = 'my_profile'

# for custom user model
AUTH_USER_MODEL = 'beerapp.CustomUser'

# for heroku migration of api
# CREDENTIALS = {
#     'api_key': os.environ.get('api_key'),
#     'api_key_1': os.environ.get('api_key_1'),
#     'client_id': os.environ.get('client_id'),
#     'client_id_1': os.environ.get('client_id_1'),
#     'client_secret': os.environ.get('client_secret'),
#     'client_secret_1': os.environ.get('CLIENT_SECRET_1'),
#     'map_api': os.environ.get('map_api')
# }

# for dev environment
CREDENTIALS = {
    'RATEBEER': {
        'API_KEY': os.environ.get('RATEBEER_API_KEY'),
        'API_KEY1': os.environ.get('RATEBEER_API_KEY1')
    },
    'UNTAPPD': {
        'CLIENT_ID': os.environ.get('UNTAPPD_CLIENT_ID'),
        'CLIENT_SECRET': os.environ.get('UNTAPPD_CLIENT_SECRET'),
        'CLIENT_ID1': os.environ.get('UNTAPPD_CLIENT_ID1'),
        'CLIENT_SECRET': os.environ.get('UNTAPPD_CLIENT_SECRET1')
    },
    'GOOGLE': {
        'MAP_API': os.environ.get('MAP_API_KEY')
    }
}