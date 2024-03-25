from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False if os.environ.get('DEBUG') == 'False' else True
# DEBUG = os.environ.get('DEBUG') == True  # noqa: E712
# DEBUG = True
# DEBUG = False
# DEBUG = True if os.environ.get('DEBUG') else False
# DEBUG = True if os.getenv('DEBUG') == 'True' else False

ALLOWED_HOSTS = ['127.0.0.1', os.getenv('webserver'), 'webserver']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'django_filters',
    'django_extensions',
    # 'shell_plus',
    'task_manager',
    'task_manager.user',
    'task_manager.label',
    'task_manager.status',
    'task_manager.task',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'task_manager.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: E501
    },
]

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'

LANGUAGES = [
    # ('en', 'English'),
    ('ru', 'Russian'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

STATIC_URL = os.getenv('static_url')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BOOTSTRAP5 = {
    "css_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css",  # noqa: E501
        "integrity": "sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx",  # noqa: E501
        "crossorigin": "anonymous",
    },
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js",  # noqa: E501
        "integrity": "sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa",  # noqa: E501
        "crossorigin": "anonymous",
    },
    "theme_url": None,
    'javascript_in_head': False,
    'wrapper_class': 'mb-3',
    'inline_wrapper_class': '',
    'horizontal_label_class': 'col-sm-2',
    'horizontal_field_class': 'col-sm-10',
    'horizontal_field_offset_class': 'offset-sm-2',
    'set_placeholder': True,
    'required_css_class': '',
    'error_css_class': '',
    'success_css_class': '',
    'server_side_validation': True,
    'formset_renderers': {
        'default': 'django_bootstrap5.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'django_bootstrap5.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'django_bootstrap5.renderers.FieldRenderer',
    },
}

ROLLBAR = {
    'access_token': 'b287999df8ef48ee9a3cd3e5564d2a4a',
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}
